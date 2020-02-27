from datetime import datetime
from django.db import models
from django.apps import apps

class CapexType(models.Model):
  type = models.CharField("Tipo de Capex", max_length=255)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizadem", auto_now=True)

  def __str__(self):
    return self.type

  class Meta:
    verbose_name = 'Tipo de Capex'
    verbose_name_plural = 'Tipos de Capex'

class Capex(models.Model):
  type = models.ForeignKey(CapexType, verbose_name='Tipo de Capex', on_delete=models.CASCADE)
  # TODO: Esse qrcode deve seguir as seguintes etapas de comptactação:
  #       1 - Texto em JSON para binário
  #       2 - Binário para base64
  qrcode = models.TextField("QR Code em base64")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.type.type

  class Meta:
    verbose_name = 'Capex'
    verbose_name_plural = 'Capex'

class Expiration(models.Model):
  date = models.DateTimeField('Data de validade')

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.date)

  class Meta:
    verbose_name = 'Validade e lote'
    verbose_name_plural = 'Validades e lotes'

class Product(models.Model):
  description = models.CharField("Descrição do produto", max_length=255)
  image = models.TextField("Imagem em base64", blank=True, null=True)
  barcode = models.CharField("Código de barras", max_length=32)
  quantity = models.IntegerField("Quantidade em estoque", default=0)
  expiration = models.ManyToManyField(Expiration, verbose_name='Datas de validade e lotes', blank=True)
  invoices = models.ManyToManyField('invoice.Invoice', verbose_name="Notas que deram baixa neste produto", blank=True)
  isActive = models.BooleanField('Produto ativo', null=True, blank=True, default=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'

class PicklistProduct(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
  quantity = models.IntegerField("Quantidade")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.product.description

  class Meta:
    verbose_name = 'Produto de Picklist'
    verbose_name_plural = 'Produtos de Picklist'

class Picklist(models.Model):
  version = models.CharField('Versão da Picklist', max_length=32, blank=True, null=True)
  products = models.ManyToManyField(PicklistProduct)
  instalation = models.ForeignKey('micromarket.Instalation', verbose_name="Instalação", on_delete=models.SET_NULL, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    if self.version:
      return self.version
    else:
      return "Versão da picklist não especificada"

  class Meta:
    verbose_name = 'Picklist'
    verbose_name_plural = 'Picklists'

class PlanogramProductDiscount(models.Model):
  percent = models.FloatField("Desconto em (%)")
  begin = models.DateTimeField("Data e hora inicial")
  end = models.DateTimeField("Data e hora final")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    if self.percent == 100:
      return "Bonificado"
    elif self.percent == 0:
      return "Sem desconto"
    else:
      return "%f" % self.percent

  class Meta:
    verbose_name = "Desconto de itens do Planograma"
    verbose_name_plural = "Descontos de itens dos Planogramas"

class PlanogramProduct(models.Model):
  product = models.ForeignKey(Product, verbose_name="Produto da Nota Fiscal", on_delete=models.SET_NULL, null=True)
  price = models.FloatField("Preço do produto")
  discount = models.ForeignKey(PlanogramProductDiscount, verbose_name="Desconto no item do planograma", on_delete=models.SET_NULL, null=True)
  pair = models.IntegerField("Número de par")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.product.description

  class Meta:
    verbose_name = 'Produto de Planograma'
    verbose_name_plural = "Produtos de Planograma"

class Planogram(models.Model):
  version = models.CharField("Versão do Planograma", max_length=8)
  products = models.ManyToManyField(PlanogramProduct, verbose_name="Produtos do Planograma")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.version

  class Meta:
    verbose_name = 'Planograma'
    verbose_name_plural = 'Planogramas'

class Sale(models.Model):
  customer = models.CharField("Nome do cliente", max_length=120)
  token = models.CharField("Token da venda", max_length=255)
  products = models.ManyToManyField(PlanogramProduct, verbose_name="Produtos vendidos")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.token

  class Meta:
    verbose_name = 'Venda'
    verbose_name_plural = 'Vendas'

class Billet(models.Model):
  TYPE_CHOICES = (
    ('I', 'Insumo'), ('C', 'Combustível'),
    ('T', 'Transporte'), ('M', 'Material de Escritório'),
    ('TI', 'Técnico de Informática'), ('F', 'Funcionário')
  )
  OPERATION_TYPE_CHOICES = (
    ('A', 'Aporte'), ('G', 'Gasto')
  )

  type = models.CharField('Tipo de conta', max_length=2, choices=TYPE_CHOICES)
  operation = models.CharField('Tipo de operação', max_length=1, choices=OPERATION_TYPE_CHOICES)
  value = models.FloatField('Valor', default=0)
  receipt = models.TextField('Foto do recibo (em base64)', blank=True, null=True)
  description = models.CharField('Observação', max_length=255)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.operation

  class Meta:
    verbose_name = 'Conta a pagar'
    verbose_name_plural = 'Contas a pagar'
