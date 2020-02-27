import uuid

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.contrib.humanize.templatetags.humanize import naturalday
from datetime import datetime, timedelta

from . import serializers
from . import models

import holidays

from services.invoice import models as invoice

class CapexTypeViewSet(viewsets.ModelViewSet):
  queryset = models.CapexType.objects.all()
  serializer_class = serializers.CapexTypeSerializer
  filter_backends = [DjangoFilterBackend]

class CapexViewSet(viewsets.ModelViewSet):
  queryset = models.Capex.objects.all()
  serializer_class = serializers.CapexSerializer
  filter_backends = [DjangoFilterBackend]

class ProductViewSet(viewsets.ModelViewSet):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductSerializer
  filter_backends = [DjangoFilterBackend]
  filter_fields = {
    "id": ["exact"]
  }

  @action(detail=False, methods=['put'], url_path="update-image")
  def _update_image(self, request):
    id = int(request.data['id'])
    image = request.data['image']

    try:
      product = models.Product.objects.get(pk=id)
      product.image = image
      product.save()
    except Exception as ex:
      raise ValidationError({
        "type": "SaveError",
        "message": "Ocorreu um erro ao salvar a nova imagem no servidor.",
        "proper": ex
      })

    return Response({
      "type": "UpdateProductImage",
      "message": "Imagem alterada com sucesso."
    })

  @action(detail=False, methods=['get'], url_path="flat-resource")
  def _get_flat_resource(self, request):
    products = models.Product.objects.values_list('id', 'quantity', 'barcode', 'description').order_by('barcode')
    bundles = list(map(lambda item: {'id': item[0], 'stock_quantity': item[1], 'barcode': item[2], 'description': item[3], 'average_price': 0 }, products))

    for index, bundle in enumerate(bundles):
      planogram_products = models.PlanogramProduct.objects.filter(product__pk=bundle['id'])
      for planogram_product in planogram_products:
        bundles[index]['average_price'] += planogram_product.price
      if planogram_products:
        bundles[index]['average_price'] /= len(planogram_products)

    return Response(bundles)

  @action(detail=False, methods=['get'], url_path="grow-resource")
  def _get_grow_resource(self, request):
    id = int(request.query_params.get("id"))
    product = models.Product.objects.get(pk=id)

    issuers = list()
    for invoice in product.invoices.all():
      if not invoice.issuer.tradeName in issuers:
        issuers.append(invoice.issuer.tradeName)

    response = dict(
      id=product.pk,
      image=product.image,
      issuers=issuers,
      description=product.description,
      barcode=product.barcode,
      expiration=[naturalday(expiration.date) for expiration in product.expiration.all()],
      stock_quantity=product.quantity,
      isActive=product.isActive
    )

    return Response(response)

  @action(detail=False, methods=['get'], url_path="expiration/close")
  def _get_expiration_close(self, request):
    holidays_br = holidays.CountryHoliday('BR', prov=None, state='RJ')

    if 'limit_day' in request.data.keys():
      limit_expiration_count = int(request.data["limit_day"])
    else:
      limit_expiration_count = 3650

    responses = list()
    today = datetime.today()
    limit_day = today + timedelta(days=limit_expiration_count)
    products = models.Product.objects.filter(expiration__date__gte=today, expiration__date__lte=limit_day)

    # desmembra todas as validades da instancia a partir do filtro para poder criar uma lista
    for product in products:
      expirations = product.expiration.filter(date__gte=today, date__lte=limit_day)
      expiration_response = dict(
        # data exata do vencimento
        strict=list(),
        # data exata do vencimento humanizada
        natural=list(),
        # dias em que o popup será mostrado
        show_until=list()
      )
      for expiration in expirations:
        show_until = expiration.date
        # verifica se a validade cai em um feriado
        if show_until in holidays_br:
          show_until += timedelta(days=1)
        # verifica se a data de validade cairá no final de semana
        if show_until.weekday() >= 5:
          show_until += timedelta(days=7 - show_until.weekday())

        expiration_response["strict"].append(expiration.date)
        expiration_response["natural"].append(naturalday(expiration.date))
        expiration_response["show_until"].append(show_until)

      # remove as datas repetidas
      expiration_response["strict"] = list(dict.fromkeys(expiration_response["strict"]))
      expiration_response["strict"].sort()
      expiration_response["natural"] = list(dict.fromkeys(expiration_response["natural"]))
      expiration_response["natural"].sort()
      expiration_response["show_until"] = list(dict.fromkeys(expiration_response["show_until"]))
      expiration_response["show_until"].sort()

      response = dict(
        description=product.description,
        expirations=expiration_response,
        barcode=product.barcode
      )
      responses.append(response)
    return Response(responses)

  @action(detail=False, methods=['post'], url_path="create/from/invoice")
  def _create_from_invoice(self, request):
    '''
      Dados requeridos em lista dentro do request.data:
        1. description
        3. stock_quantity
        4. invoice_quantity
        5. barcode
        6. image
        7. exists
    '''

    # Valida o formulário de entrega dos dados
    for item in request.data:
      if not 'barcode' in item.keys():
        raise ValidationError({
          'message': 'Não é possível cadastrar o produto sem código de barras'
        })
      if not item["barcode"].strip():
        return Response({ "type": "error", "message": "O produto '%s' não tem código de barras" })

    # Cadastra os produtos
    for item in request.data:
      # Insere uma imagem padrão para o produto que não tem Imagem
      if item["image"] is None:
        item["image"] = '''data:image/png;base64,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
        '''
      accessKey = item.pop("accessKey")
      invoiceModel = invoice.Invoice.objects.get(protocol__accessKey=accessKey)
      # Adiciona validades ao produto
      expirations = list()
      for expiration in item.pop("expiration"):
        expiration_model = models.Expiration(date=expiration["validity"])
        expiration_model.save()
        expirations.append(expiration_model)
      # Verifica se o produto existe
      if item.pop("exists"):
        product = models.Product.objects.get(barcode=item["barcode"])
        product.quantity += item.pop("invoice_quantity")
      else:
        item["quantity"] = item.pop("invoice_quantity")
        item.pop("stock_quantity")
        product = models.Product(**item)
      product.save()

      product.invoices.add(invoiceModel)
      for expiration in expirations:
        product.expiration.add(expiration)

    return Response(
      {"message": "Produtos da nota '%s' cadastrados." % accessKey}
    )

  @action(detail=False, methods=['put'], url_path="update")
  def _update_product(self, request):
    # HACK: A resposta do banco de dados para produtos no frontend geralmente chega
    # como 'stock_quantity' para melhor compreensão. Os dados retornados na página /produtos
    # chegam como stock_quantity e aqui alterei o nome do field para quantity.
    wise_response_data = request.data
    wise_response_data["quantity"] = wise_response_data.pop("stock_quantity")

    fields = ["id", "barcode", "quantity", "description"]
    for request_field in wise_response_data.keys():
      if not request_field in fields:
        raise ValidationError({
          "type": "UnresearchableField",
          "message": "O campo '%s' não é um campo válido." % request_field,
        })

    # HACK:
    product = models.Product.objects.filter(pk=wise_response_data["id"]).update(**wise_response_data)
    print(product)

    return Response({})

class PicklistProductViewSet(viewsets.ModelViewSet):
  queryset = models.PicklistProduct.objects.all()
  serializer_class = serializers.PicklistProductSerializer
  filter_backends = [DjangoFilterBackend]

class PicklistViewSet(viewsets.ModelViewSet):
  queryset = models.Picklist.objects.all()
  serializer_class = serializers.PicklistSerializer
  filter_backends = [DjangoFilterBackend]

  @action(detail=False, methods=['post'], url_path="create")
  def _create(self, request):
    responses = list()
    data["version"] = uuid.uuid4().hex[:8].upper()
    picklist_products_id = [int(i) for i in dict(data)['products']]
    picklist_products = models.PicklistProduct.objects.filter(pk__in=picklist_products_id)
    for pick_product in picklist_products:
      response = dict(
        id=pick_product.pk,
        description=pick_product.product.description,
        quantity=pick_product.quantity
      )
      pick_product.product.quantity -= pick_product.quantity
      pick_product.product.save()
      responses.append(response)
    return Response(responses)

  @action(detail=False, methods=['post'], url_path="cancel")
  def _cancel(self, request):
    products = request.data["products"]
    return Response({})

class PlanogramProductDiscountViewSet(viewsets.ModelViewSet):
  queryset = models.PlanogramProductDiscount.objects.all()
  serializer_class = serializers.PlanogramProductDiscountSerializer
  filter_backends = [DjangoFilterBackend]

class PlanogramProductViewSet(viewsets.ModelViewSet):
  queryset = models.PlanogramProduct.objects.all()
  serializer_class = serializers.PlanogramProductSerializer
  filter_backends = [DjangoFilterBackend]

class PlanogramViewSet(viewsets.ModelViewSet):
  queryset = models.Planogram.objects.all()
  serializer_class = serializers.PlanogramSerializer
  filter_backends = [DjangoFilterBackend]

class SaleViewSet(viewsets.ModelViewSet):
  queryset = models.Sale.objects.all()
  serializer_class = serializers.SaleSerializer
  filter_backends = [DjangoFilterBackend]

  @action(detail=False, methods=['get'], url_path="financial/balance")
  def _financial_balance(self, request):
    pass
