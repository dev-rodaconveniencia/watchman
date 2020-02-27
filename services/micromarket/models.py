from django.db import models

class Address(models.Model):
  phone = models.CharField('Telefone', max_length=16)
  state = models.CharField('Estado', max_length=80)
  city = models.CharField('Cidade', max_length=120)
  district = models.CharField("Bairro", max_length=80)
  additionalInformation = models.CharField("Complemento", max_length=80)
  streetSuffix = models.CharField("Sufixo", max_length=15)
  street = models.CharField("Rua", max_length=120)
  number = models.CharField("Número", max_length=8)
  postalCode = models.CharField("Código Postal", max_length=9)
  country = models.CharField("País", max_length=25)
  countryBacenCode = models.CharField("Código Bacen do País", max_length=4)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.street

  class Meta:
    verbose_name = 'Endereço'
    verbose_name_plural = 'Endereços'

class Checkout(models.Model):
  identifier = models.CharField("Identificador", max_length=32)
  capex = models.ManyToManyField('wharehouse.Capex', verbose_name="Capex")

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.identifier

  class Meta:
    verbose_name = "Serviço de Autopagamento"
    verbose_name = "Serviços de Autopagamento"

class Instalation(models.Model):
  contact = models.CharField("Responsável pela instalação", max_length=120)
  email = models.CharField("E-mail para contato", max_length=255)
  identifier = models.CharField("Identificador", max_length=32)
  checkout = models.ForeignKey(Checkout, verbose_name="Serviço de Autopagamento", on_delete=models.SET_NULL, null=True)
  capex = models.ManyToManyField('wharehouse.Capex', verbose_name="capex")
  address = models.ForeignKey(Address, verbose_name="Endereço", on_delete=models.SET_NULL, null=True)
  planogram = models.ForeignKey('wharehouse.Planogram', verbose_name="Planograma", on_delete=models.SET_NULL, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.identifier

  class Meta:
    verbose_name = 'Instalação'
    verbose_name_plural = 'Instalações'
