from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

import base64

from . import serializers
from . import models

from services.wharehouse import models as wharehouse
from services.invoice import models as watchman_invoice
from services.business import nfeio, cosmos, vmpay, sefaz

class CityViewSet(viewsets.ModelViewSet):
  queryset = models.City.objects.all()
  serializer_class = serializers.CitySerializer
  filter_backends = [DjangoFilterBackend]

class AddressViewSet(viewsets.ModelViewSet):
  queryset = models.Address.objects.all()
  serializer_class = serializers.AddressSerializer
  filter_backends = [DjangoFilterBackend]

class CardViewSet(viewsets.ModelViewSet):
  queryset = models.Card.objects.all()
  serializer_class = serializers.CardSerializer
  filter_backends = [DjangoFilterBackend]

class PaymentDetailViewSet(viewsets.ModelViewSet):
  queryset = models.PaymentDetail.objects.all()
  serializer_class = serializers.PaymentDetailSerializer
  filter_backends = [DjangoFilterBackend]

class PaymentViewSet(viewsets.ModelViewSet):
  queryset = models.Payment.objects.all()
  serializer_class = serializers.PaymentSerializer
  filter_backends = [DjangoFilterBackend]

class DuplicatesViewSet(viewsets.ModelViewSet):
  queryset = models.Duplicates.objects.all()
  serializer_class = serializers.DuplicatesSerializer
  filter_backends = [DjangoFilterBackend]

class BillViewSet(viewsets.ModelViewSet):
  queryset = models.Bill.objects.all()
  serializer_class = serializers.BillSerializer
  filter_backends = [DjangoFilterBackend]

class BillingViewSet(viewsets.ModelViewSet):
  queryset = models.Billing.objects.all()
  serializer_class = serializers.BillingSerializer
  filter_backends = [DjangoFilterBackend]

class FuelPumpViewSet(viewsets.ModelViewSet):
  queryset = models.FuelPump.objects.all()
  serializer_class = serializers.FuelPumpSerializer
  filter_backends = [DjangoFilterBackend]

class FuelCideViewSet(viewsets.ModelViewSet):
  queryset = models.FuelCide.objects.all()
  serializer_class = serializers.FuelCideSerializer
  filter_backends = [DjangoFilterBackend]

class FuelViewSet(viewsets.ModelViewSet):
  queryset = models.Fuel.objects.all()
  serializer_class = serializers.FuelSerializer
  filter_backends = [DjangoFilterBackend]

class MedicineDetailViewSet(viewsets.ModelViewSet):
  queryset = models.MedicineDetail.objects.all()
  serializer_class = serializers.MedicineDetailSerializer
  filter_backends = [DjangoFilterBackend]

class TaxICMSDestinationViewSet(viewsets.ModelViewSet):
  queryset = models.TaxICMSDestination.objects.all()
  serializer_class = serializers.TaxICMSDestinationSerializer
  filter_backends = [DjangoFilterBackend]

class TaxCOFINSViewSet(viewsets.ModelViewSet):
  queryset = models.TaxCOFINS.objects.all()
  serializer_class = serializers.TaxCOFINSSerializer
  filter_backends = [DjangoFilterBackend]

class TaxPISViewSet(viewsets.ModelViewSet):
  queryset = models.TaxPIS.objects.all()
  serializer_class = serializers.TaxPISSerializer
  filter_backends = [DjangoFilterBackend]

class TaxIIViewSet(viewsets.ModelViewSet):
  queryset = models.TaxII.objects.all()
  serializer_class = serializers.TaxIISerializer
  filter_backends = [DjangoFilterBackend]

class TaxIPIViewSet(viewsets.ModelViewSet):
  queryset = models.TaxIPI.objects.all()
  serializer_class = serializers.TaxIPISerializer
  filter_backends = [DjangoFilterBackend]

class TaxICMSViewSet(viewsets.ModelViewSet):
  queryset = models.TaxICMS.objects.all()
  serializer_class = serializers.TaxICMSSerializer
  filter_backends = [DjangoFilterBackend]

class TaxViewSet(viewsets.ModelViewSet):
  queryset = models.Tax.objects.all()
  serializer_class = serializers.TaxSerializer
  filter_backends = [DjangoFilterBackend]

class ItemViewSet(viewsets.ModelViewSet):
  queryset = models.Item.objects.all()
  serializer_class = serializers.ItemsSerializer
  filter_backends = [DjangoFilterBackend]

class ProtocolViewSet(viewsets.ModelViewSet):
  queryset = models.Protocol.objects.all()
  serializer_class = serializers.ProtocolSerializer
  filter_backends = [DjangoFilterBackend]

class ReferencedProcessViewSet(viewsets.ModelViewSet):
  queryset = models.ReferencedProcess.objects.all()
  serializer_class = serializers.ReferencedProcessSerializer
  filter_backends = [DjangoFilterBackend]

class TaxpayerCommentsViewSet(viewsets.ModelViewSet):
  queryset = models.TaxpayerComments.objects.all()
  serializer_class = serializers.TaxpayerCommentsSerializer
  filter_backends = [DjangoFilterBackend]

class DocumentInvoiceReferenceViewSet(viewsets.ModelViewSet):
  queryset = models.DocumentInvoiceReference.objects.all()
  serializer_class = serializers.DocumentInvoiceReferenceSerializer
  filter_backends = [DjangoFilterBackend]

class TaxCouponInformationViewSet(viewsets.ModelViewSet):
  queryset = models.TaxCouponInformation.objects.all()
  serializer_class = serializers.TaxCouponInformationSerializer
  filter_backends = [DjangoFilterBackend]

class TaxDocumentsReferenceViewSet(viewsets.ModelViewSet):
  queryset = models.TaxDocumentsReference.objects.all()
  serializer_class = serializers.TaxDocumentsReferenceSerializer
  filter_backends = [DjangoFilterBackend]

class AdditionalInformationViewSet(viewsets.ModelViewSet):
  queryset = models.AdditionalInformation.objects.all()
  serializer_class = serializers.AdditionalInformationSerializer
  filter_backends = [DjangoFilterBackend]

class TransportRateViewSet(viewsets.ModelViewSet):
  queryset = models.TransportRate.objects.all()
  serializer_class = serializers.TransportRateSerializer
  filter_backends = [DjangoFilterBackend]

class TransportVehicleViewSet(viewsets.ModelViewSet):
  queryset = models.TransportVehicle.objects.all()
  serializer_class = serializers.TransportVehicleSerializer
  filter_backends = [DjangoFilterBackend]

class TransportVolumeViewSet(viewsets.ModelViewSet):
  queryset = models.TransportVolume.objects.all()
  serializer_class = serializers.TransportVolumeSerializer
  filter_backends = [DjangoFilterBackend]

class TransportReboqueViewSet(viewsets.ModelViewSet):
  queryset = models.TransportReboque.objects.all()
  serializer_class = serializers.TransportReboqueSerializer
  filter_backends = [DjangoFilterBackend]

class TransportGroupViewSet(viewsets.ModelViewSet):
  queryset = models.TransportGroup.objects.all()
  serializer_class = serializers.TransportGroupSerializer
  filter_backends = [DjangoFilterBackend]

class TransportViewSet(viewsets.ModelViewSet):
  queryset = models.Transport.objects.all()
  serializer_class = serializers.TransportSerializer
  filter_backends = [DjangoFilterBackend]

class TotalsISSQNViewSet(viewsets.ModelViewSet):
  queryset = models.TotalsISSQN.objects.all()
  serializer_class = serializers.TotalsISSQNSerializer
  filter_backends = [DjangoFilterBackend]

class TotalsICMSViewSet(viewsets.ModelViewSet):
  queryset = models.TotalsICMS.objects.all()
  serializer_class = serializers.TotalsICMSSerializer
  filter_backends = [DjangoFilterBackend]

class TotalsViewSet(viewsets.ModelViewSet):
  queryset = models.Totals.objects.all()
  serializer_class = serializers.TotalsSerializer
  filter_backends = [DjangoFilterBackend]

class BuyerViewSet(viewsets.ModelViewSet):
  queryset = models.Buyer.objects.all()
  serializer_class = serializers.BuyerSerializer
  filter_backends = [DjangoFilterBackend]

class IssuerViewSet(viewsets.ModelViewSet):
  queryset = models.Issuer.objects.all()
  serializer_class = serializers.IssuerSerializer
  filter_backends = [DjangoFilterBackend]

class InvoiceViewSet(viewsets.ModelViewSet):
  queryset = models.Invoice.objects.all()
  serializer_class = serializers.InvoiceSerializer
  filter_backends = [DjangoFilterBackend]

  @action(detail=False, methods=['get'], url_path="check")
  def check(self, request):
    '''
      Este método busca informações sobre as notas fiscais da NFEio.

      Parameters
      ==========
      accessKey : string
        Chave de acesso da nota fiscal eletrônica

      Return
      ==========
      Response(invoice)
        Nota fiscal eletrônica crua da NFEio
        (ver documentação em https://nfe.io/docs/)
    '''
    accessKey = request.query_params.get('accessKey')
    invoice = nfeio.search(accessKey)
    safe = "data:application/octet-stream;charset=utf-16le;base64,"
    invoice["xml"] = {
      "base64" : safe + base64.b64encode(nfeio.xml(accessKey)).decode('utf-8')
    }
    return Response(invoice)

  @action(detail=False, methods=['post'], url_path="receive")
  def receive(self, request):
    '''
      Este método recebe a nota fiscal e a cadastra caso não tenha sido cadastrada.
      Retorna uma lista com todos os possíveis itens para cadastro.

      Parameters
      ==========
      accessKey : string
        Chave de acesso da nota fiscal eletrônica
      type : string
        Tipo de nota fiscal

      Return
      ==========
      Response([{
        description : string
          Descrição do produto
        stock_quantity : int
          Quantidade em estoque
        invoice_quantity : int
          Quantidade na nota fiscal
        barcode : string
          Código de barras
        image : string
          Imagem em base64
        exists : boolean
          Verificador caso exista ou  não o produto
      }])
    '''
    # Recebe a chave de acesso da nota fiscal
    # expirations = request.data['expirations']
    accessKey = request.data['accessKey']
    type = request.data['type']
    # Itens que irão retornar para o segundo passo do cadastro
    items = list()
    if not models.Protocol.objects.filter(accessKey=accessKey).exists():
      # Recebe a nota da NFEio
      invoice = nfeio.search(accessKey)
      invoice["type"] = type

      if type != "Insumo":
        invoice["isPending"] = False

      serializer = serializers.InvoiceSerializer(data=invoice)
      if serializer.is_valid(raise_exception=True):
        if type != 'Insumo':
          return Response({
            'type': 'VoidResponse',
            'message': 'Nota fiscal "%s" cadastrada com sucesso' % accessKey
          })

        # Salva a nota fiscal para obter o pk do item referente
        instance = serializer.save()

        # Cria uma lista de produtos a partir dos itens da nota fiscal
        for item in serializer.validated_data["items"]:
          item_model = dict()
          item_model["accessKey"] = accessKey
          product = wharehouse.Product.objects.filter(
            invoices__items__code=item['code']
          )
          if product.exists():
            # Retorna as informações do banco e a a quantidade em nota
            product = product.first()
            item_model["description"] = product.description.title()
            item_model["stock_quantity"] = product.quantity
            item_model["invoice_quantity"] = item["quantity"]
            item_model["barcode"] = product.barcode
            item_model["image"] = product.image
            item_model["exists"] = True
          else:
            # Retorna as informações da nota e a imagem do Cosmos se houver
            item_model["description"] = item["description"].title()
            item_model["stock_quantity"] = 0
            item_model["invoice_quantity"] = item["quantity"]
            item_model["barcode"] = item["codeGTIN"]
            item_model["image"] = cosmos.search.image(item["codeGTIN"])
            item_model["exists"] = False
          items.append(item_model)
        return Response(items)
    else:
      raise ValidationError({
        "type": "AlreadyRegisteredInvoice",
        "message" : "A nota fiscal %s já foi cadastrada." % accessKey
        })

  @action(detail=False, methods=['get'], url_path="search/sefaz")
  def _search_sefaz(self, request):
    company = request.user.company
    from pprint import pprint as print
    # 33200142498675000152558900024806661493478221
    nfe = sefaz.nfe(
      pfxpath=company.certificate_file.path,
      password=company.certificate_password,
      cnpj=company.cnpj
    )
    print(nfe._nsu_range())
    # print(user)
    return Response({})
