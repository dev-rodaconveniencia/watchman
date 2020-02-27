from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models

class City(models.Model):
  code = models.CharField('Código', max_length=7, blank=True, null=True)
  name = models.CharField('Nome', max_length=120, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Cidade'
    verbose_name_plural = 'Cidades'

class Address(models.Model):
  phone = models.CharField('Telefone', max_length=16, blank=True, null=True)
  state = models.CharField('Estado', max_length=80, blank=True, null=True)
  city = models.ForeignKey(City, verbose_name='Cidade', on_delete=models.SET_NULL, null=True, blank=True)
  district = models.CharField("Bairro", max_length=80, blank=True, null=True)
  additionalInformation = models.CharField("Complemento", max_length=80, blank=True, null=True)
  streetSuffix = models.CharField("Sufixo", max_length=15, blank=True, null=True)
  street = models.CharField("Rua", max_length=120, blank=True, null=True)
  number = models.CharField("Número", max_length=32, blank=True, null=True)
  postalCode = models.CharField("Código Postal", max_length=9, blank=True, null=True)
  country = models.CharField("País", max_length=25, blank=True, null=True)
  countryBacenCode = models.CharField("Código Bacen do País", max_length=10, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Endereço'
    verbose_name_plural = 'Endereços'

class Card(models.Model):
  federalTaxNumber = models.CharField("CNPJ da Credenciadora de cartão de crédito e/ou débito ", max_length=44, blank=True, null=True)
  flag = models.CharField("Bandeira da operadora de cartão de crédito e/ou débito", max_length=44, blank=True, null=True)
  authorization = models.CharField("Número de autorização da operação cartão de crédito e/ou débito", max_length=44, blank=True, null=True)
  integrationPaymentType = models.CharField("Tipo de Integração para pagamento", max_length=44, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Cartão'
    verbose_name_plural = 'Cartões'

class PaymentDetail(models.Model):
  method = models.CharField("Forma de pagamento", max_length=44, blank=True, null=True)
  amount = models.CharField("Valor do pagamento", max_length=44, blank=True, null=True)
  card = models.ForeignKey(Card, verbose_name="Cartão", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Detalhe do Pagamento'
    verbose_name_plural = 'Detalhes dos pagamentos'

class Payment(models.Model):
  paymentDetail = models.ManyToManyField(PaymentDetail, verbose_name="Detalhe do pagamento", blank=True)
  payBack = models.FloatField("Valor do troco", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.payBack)

  class Meta:
    verbose_name = 'Pagamento'
    verbose_name_plural = 'Pagamentos'

class Duplicates(models.Model):
  duplicateNumber = models.CharField("Número da Duplicata", max_length=44, blank=True, null=True)
  expirationOn = models.DateTimeField("Data de vencimento", blank=True, null=True)
  amount = models.CharField("Valor da duplicata", max_length=44, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Duplicata'
    verbose_name_plural = 'Duplicatas'

class Bill(models.Model):
  number = models.CharField("Número da Fatura", max_length=255, blank=True, null=True)
  originalAmount = models.FloatField("Valor Original da Fatura", blank=True, null=True)
  discountAmount = models.FloatField("Valor do desconto", blank=True, null=True)
  netAmount = models.FloatField("Valor Líquido da Fatura", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Fatura'
    verbose_name_plural = 'Faturas'

class Billing(models.Model):
  bill = models.ForeignKey(Bill, verbose_name="Fatura", on_delete=models.SET_NULL, null=True, blank=True)
  duplicates = models.ManyToManyField(Duplicates, verbose_name="Duplicatas", blank=True)

  def __str__(self):
    return self.bill.number

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Cobrança'
    verbose_name_plural = 'Cobranças'

class FuelPump(models.Model):
  spoutNumber = models.FloatField("Número de identificação do bico utilizado no abastecimento", blank=True, null=True)
  number = models.FloatField("Número de identificação da bomba ao qual o bico está interligado", blank=True, null=True)
  tankNumber = models.FloatField("Número de identificação do tanque ao qual o bico está interligado", blank=True, null=True)
  beginningAmount = models.FloatField("Valor do Encerrante no início do abastecimento", blank=True, null=True)
  endAmount = models.FloatField("Valor do Encerrante no final do abastecimento", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Informação do grupo de “encerrante”'
    verbose_name_plural = 'Informações do grupo de “encerrante”'

class FuelCide(models.Model):
  bc = models.FloatField("BC da CIDE", blank=True, null=True)
  rate = models.FloatField("Valor da alíquota da CIDE", blank=True, null=True)
  cideAmount = models.FloatField("Valor da CIDE", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Informação da CIDE'
    verbose_name_plural = 'Informações da CIDE'

class Fuel(models.Model):
  codeANP = models.CharField("Código de produto da ANP", max_length=32, blank=True, null=True)
  percentageNG = models.FloatField("Percentual de Gás Natural para o produto GLP", blank=True, null=True)
  descriptionANP = models.CharField("Descrição do produto conforme ANP", max_length=255, blank=True, null=True)
  percentageGLP = models.FloatField("Percentual do GLP derivado do petróleo no produto GLP", blank=True, null=True)
  percentageNGn = models.FloatField("Percentual de Gás Natural Nacional", blank=True, null=True)
  percentageGNi = models.FloatField("Percentual de Gás Natural Importado", blank=True, null=True)
  startingAmount = models.FloatField("Valor de partida", blank=True, null=True)
  codif = models.CharField("Código de autorização/registro do CODIF", max_length=120, blank=True, null=True)
  amountTemp = models.FloatField("Quantidade de combustível faturada à temperatura ambiente", blank=True, null=True)
  stateBuyer = models.CharField("Sigla da UF de consumo", max_length=120, blank=True, null=True)
  cide = models.ForeignKey(FuelCide, verbose_name="Contribuição de Intervenção do Domínio Econômico", on_delete=models.SET_NULL, null=True, blank=True)
  pump = models.ForeignKey(FuelPump, verbose_name="Grupo de Encerrante", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = "Imposto sobre Combustível"
    verbose_name_plural = 'Impostos sobre Combustível'

class MedicineDetail(models.Model):
  maximumPrice = models.IntegerField("Preço máximo consumidor", blank=True, null=True)
  anvisaCode = models.CharField("Código de Produto da ANVISA", max_length=80, blank=True, null=True)
  batchId = models.CharField("Número do Lote de medicamentos ou de matérias-primas farmacêuticas", max_length=80, blank=True, null=True)
  batchQuantity = models.IntegerField("Quantidade de produto no Lote de medicamentos ou de matérias-primas farmacêuticas", blank=True, null=True)
  manufacturedOn = models.DateTimeField("Data de fabricação", blank=True, null=True)
  expireOn = models.DateTimeField("Data de validade", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Detalhamento de Medicamento'
    verbose_name_plural = 'Detalhamento de Medicamentos'

class TaxICMSDestination(models.Model):
  vBCUFDest = models.FloatField("Valor da Base de Cálculo do ICMS na UF de destino.", blank=True, null=True)
  pFCPUFDest = models.FloatField("Percentual adicional inserido na alíquota interna da UF de destino, relativo ao Fundo de Combate à Pobreza (FCP) naquela UF", blank=True, null=True)
  pICMSUFDest = models.FloatField("Alíquota adotada nas operações internas na UF de destino para o produto/mercadoria", blank=True, null=True)
  pICMSInter = models.FloatField("Alíquota interestadual das UF envolvidas", blank=True, null=True)
  pICMSInterPart = models.FloatField("Percentual de ICMS Interestadual para a UF de destino", blank=True, null=True)
  vFCPUFDest = models.FloatField("Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino", blank=True, null=True)
  vICMSUFDest = models.FloatField("Valor do ICMS Interestadual para a UF de destino", blank=True, null=True)
  vICMSUFRemet = models.FloatField("Valor do ICMS Interestadual para a UF do remetente", blank=True, null=True)
  vBCFCPUFDest = models.FloatField("Valor da BC FCP na UF de destino", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Informação do ICMS Interestadual'
    verbose_name_plural = 'Informações dos ICMS\'s Interestaduais'

class TaxCOFINS(models.Model):
  cst = models.CharField("Código de Situação Tributária do PIS", max_length=32, blank=True, null=True)
  baseTax = models.FloatField("Valor da Base de Cálculo do PIS", blank=True, null=True)
  rate = models.FloatField("Alíquota do PIS (em percentual)", blank=True, null=True)
  amount = models.FloatField("Valor do PIS", blank=True, null=True)
  baseTaxProductQuantity = models.FloatField("Quantidade Vendida", blank=True, null=True)
  productRate = models.FloatField("Alíquota do PIS (em reais)", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'COFINS do Produto'
    verbose_name_plural = 'COFINS dos Produtos'

class TaxPIS(models.Model):
  cst = models.CharField("Código de Situação Tributária do PIS", max_length=32, blank=True, null=True)
  baseTax = models.FloatField("Valor da Base de Cálculo do PIS", blank=True, null=True)
  rate = models.FloatField("Alíquota do PIS (em percentual)", blank=True, null=True)
  amount = models.FloatField("Valor do PIS", blank=True, null=True)
  baseTaxProductQuantity = models.FloatField("Quantidade Vendida", blank=True, null=True)
  productRate = models.FloatField("Alíquota do PIS (em reais)", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'PIS do Produto'
    verbose_name_plural = 'PIS dos Produtos'

class TaxII(models.Model):
  baseTax = models.CharField("Valor BC do Imposto de Importação", max_length=32, blank=True, null=True)
  customsExpenditureAmount = models.CharField("Valor despesas aduaneiras", max_length=32, blank=True, null=True)
  amount = models.FloatField("Valor Imposto de Importação", blank=True, null=True)
  iofAmount = models.FloatField("Valor Imposto sobre Operações Financeiras", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Imposto de Importação'
    verbose_name_plural = 'Impostos de Importação'

class TaxIPI(models.Model):
  classification = models.CharField('Classe de enquadramento do IPI para Cigarros e Bebidas', max_length=120, blank=True, null=True)
  producerCNPJ = models.CharField('CNPJ do produtor da mercadoria, quando diferente do emitente. Somente para os casos de exportação direta ou indireta.', max_length=120, blank=True, null=True)
  stampCode = models.CharField('Código do selo de controle IPI', max_length=120, blank=True, null=True)
  stampQuantity = models.FloatField('Quantidade de selo de controle', blank=True, null=True)
  classificationCode = models.CharField('Código de Enquadramento Legal do IPI', max_length=120, blank=True, null=True)
  cst = models.CharField('Código da situação tributária do IPI', max_length=120, blank=True, null=True)
  base = models.CharField('Valor da BC do IPI', max_length=120, blank=True, null=True)
  rate = models.FloatField('Alíquota do IPI', blank=True, null=True)
  unitQuantity = models.FloatField('Quantidade total na unidade padrão para tributação (somente para os produtos tributados por unidade)', blank=True, null=True)
  unitAmount = models.FloatField('Valor por Unidade Tributável', blank=True, null=True)
  amount = models.FloatField('Valor IPI', blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'IPI do Produto'
    verbose_name_plural = 'IPI\'s dos Produtos'

class TaxICMS(models.Model):
  origin = models.CharField("Origem da mercadoria", max_length=120, blank=True, null=True)
  cst = models.CharField("Tributação do ICMS", max_length=120, blank=True, null=True)
  baseTaxModality = models.CharField("Modalidade de determinação da BC do ICMS", max_length=120, blank=True, null=True)
  baseTax = models.FloatField("Valor da BC do ICMS", blank=True, null=True)
  baseTaxSTModality = models.CharField("Modalidade de determinação da BC do ICMS ST", max_length=120, blank=True, null=True)
  baseTaxSTReduction = models.FloatField("Percentual da Redução de BC do ICMS ST", blank=True, null=True)
  baseTaxSTAmount = models.FloatField("Valor da BC do ICMS ST", blank=True, null=True)
  baseTaxReduction = models.FloatField("Percentual da Redução de BC", blank=True, null=True)
  stRate = models.FloatField("Alíquota do imposto do ICMS ST", blank=True, null=True)
  stAmount = models.FloatField("Valor do ICMS ST", blank=True, null=True)
  stMarginAmount = models.FloatField("Percentual da margem de valor Adicionado do ICMS ST", blank=True, null=True)
  csosn = models.CharField("Código de Situação da Operação", max_length=120, blank=True, null=True)
  rate = models.FloatField("Alíquota do imposto", blank=True, null=True)
  amount = models.FloatField("Valor do ICMS", blank=True, null=True)
  snCreditRate = models.CharField("Alíquota aplicável de cálculo do crédito (Simples Nacional)", max_length=120, blank=True, null=True)
  snCreditAmount = models.CharField("Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Simples Nacional)", max_length=120, blank=True, null=True)
  stMarginAddedAmount = models.CharField("Percentual da margem de valor Adicionado do ICMS ST", max_length=120, blank=True, null=True)
  stRetentionAmount = models.CharField("Valor do ICMS ST/Valor do ICMS ST cobrado anteriormente por ST", max_length=120, blank=True, null=True)
  baseSTRetentionAmount = models.CharField("Valor da BC do ICMS ST retido", max_length=120, blank=True, null=True)
  baseTaxOperationPercentual = models.CharField("Imposto Base Percentual da Operação", max_length=120, blank=True, null=True)
  ufst = models.CharField("UF para qual é devido o ICMS ST", max_length=120, blank=True, null=True)
  amountSTUnfounded = models.FloatField("Valor ICMS Desonerado", blank=True, null=True)
  amountSTReason = models.CharField("Motivo Desoneração ICMS", max_length=120, blank=True, null=True)
  baseSNRetentionAmount = models.CharField("Valor da BC do ICMS ST retido", max_length=120, blank=True, null=True)
  snRetentionAmount = models.CharField("Valor do ICMS ST retido", max_length=120, blank=True, null=True)
  amountOperation = models.CharField("Valor do ICMS da Operação", max_length=120, blank=True, null=True)
  percentualDeferment = models.CharField("Percentual do Diferimento", max_length=120, blank=True, null=True)
  baseDeferred = models.CharField("Valor do ICMS Diferido", max_length=120, blank=True, null=True)
  fcpRate = models.FloatField("Percentual do FCP - Valor do ICMS relativo ao Fundo de Combate à Pobreza (pFCP) (Percentual máximo permitido é 2%)", blank=True, null=True)
  fcpAmount = models.FloatField("Valor Total do FCP - Valor do ICMS relativo ao Fundo de Combate à Pobreza (vFCP)", blank=True, null=True)
  fcpstRate = models.FloatField("Percentual do FCP retido por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (pFCPST) retido por substituição tributária.", blank=True, null=True)
  fcpstAmount = models.FloatField("Valor Total do FCP retido por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (vFCPST) retido por substituição tributária.", blank=True, null=True)
  fcpstRetRate = models.FloatField("Percentual do FCP retido por anteriormente por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (pFCPSTRet) retido anteriormente por substituição tributária.", blank=True, null=True)
  fcpstRetAmount = models.FloatField("Valor Total do FCP retido por anteriormente por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (vFCPSTRet) retido anteriormente por substituição tributária.", blank=True, null=True)
  bcfcpstAmount = models.FloatField("Informar o valor da Base de Cálculo do FCP", blank=True, null=True)
  finalConsumerRate = models.FloatField("Modalidade de determinação da BC do ICMS", blank=True, null=True)
  bcstRetIssuerAmount = models.FloatField("Valor do BC do ICMS ST retido na UF remetente", blank=True, null=True)
  stRetIssuerAmout = models.FloatField("Valor do ICMS ST retido na UF remetente", blank=True, null=True)
  bcstBuyerAmount = models.FloatField("Valor da BC do ICMS ST da UF destino", blank=True, null=True)
  stBuyerAmout = models.FloatField("Valor do ICMS ST da UF destino", blank=True, null=True)
  substituteAmount = models.FloatField("Valor do ICMS próprio do Substituto", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'ICMS do Produto'
    verbose_name_plural = 'ICMS\' de Produtos'

class Tax(models.Model):
  totalTax = models.FloatField("Tributos incidentes no Produto ou Serviço", blank=True, null=True)
  icms = models.ForeignKey(TaxICMS, verbose_name="Dados do ICMS Normal e ST", on_delete=models.SET_NULL, null=True, blank=True)
  ipi = models.ForeignKey(TaxIPI, verbose_name="Grupo IPI", on_delete=models.SET_NULL, null=True, blank=True)
  ii = models.ForeignKey(TaxII, verbose_name="Grupo Imposto de Importação", on_delete=models.SET_NULL, null=True, blank=True)
  pis = models.ForeignKey(TaxPIS, verbose_name="Grupo PIS", on_delete=models.SET_NULL, null=True, blank=True)
  cofins = models.ForeignKey(TaxCOFINS, verbose_name="Grupo COFINS", on_delete=models.SET_NULL, null=True, blank=True)
  icmsDestination = models.ForeignKey(TaxICMSDestination, verbose_name="Informação do ICMS Interestadual", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.totalTax)

  class Meta:
    verbose_name = 'Tributo incidente no Produto ou Serviço'
    verbose_name_plural = 'Tributos incidentes no Produto ou Serviço'

class Item(models.Model):
  code = models.CharField("Código do produto ou serviço", max_length=32, blank=True, null=True)
  codeGTIN = models.CharField("GTIN (Global Trade Item Number) do produto, antigo código EAN ou código de barras (cEAN)", max_length=32, blank=True, null=True)
  description = models.CharField("Descrição do produto ou serviço", max_length=255, blank=True, null=True)
  ncm = models.CharField("Código NCM com 8 dígitos ou 2 dígitos", max_length=32, blank=True, null=True)
  extipi = models.CharField("EX_TIPI", max_length=32, blank=True, null=True)
  cfop = models.IntegerField("Código Fiscal de Operações e Prestações", blank=True, null=True)
  unit = models.CharField("Unidade Comercial", max_length=32, blank=True, null=True)
  quantity = models.FloatField("Quantidade Comercial", blank=True, null=True)
  unitAmount = models.FloatField("Valor Unitário de Comercialização", blank=True, null=True)
  totalAmount = models.FloatField("Valor Total Bruto dos Produtos ou Serviços", blank=True, null=True)
  eanTaxableCode = models.CharField("GTIN (Global Trade Item Number) da unidade tributável, antigo código EAN ou código de barras", max_length=32, blank=True, null=True)
  unitTax = models.CharField("Unidade Tributável", max_length=32, blank=True, null=True)
  quantityTax = models.FloatField("Quantidade Tributável", blank=True, null=True)
  taxUnitAmount = models.FloatField("Valor Unitário de tributação", blank=True, null=True)
  freightAmount = models.FloatField("Valor Total do Frete", blank=True, null=True)
  insuranceAmount = models.FloatField("Valor Total do Seguro", blank=True, null=True)
  discountAmount = models.FloatField("Valor do Desconto", blank=True, null=True)
  othersAmount = models.FloatField("Outras despesas acessórias", blank=True, null=True)
  totalIndicator = models.BooleanField("Indica se valor do Item entra no valor total da NF-e")
  cest = models.CharField("Código especificador da substituição tributária", max_length=32, blank=True, null=True)
  tax = models.ForeignKey(Tax, verbose_name="Tributos incidentes no Produto ou Serviço", on_delete=models.SET_NULL, null=True, blank=True)
  additionalInformation = models.TextField("Informações Adicionais do Produto", blank=True, null=True)
  numberOrderBuy = models.CharField("Número do pedido de compra", max_length=32, blank=True, null=True)
  itemNumberOrderBuy = models.IntegerField("Item do Pedido de Compra", blank=True, null=True)
  medicineDetail = models.ForeignKey(MedicineDetail, verbose_name="Detalhamento de Medicamentos e de matérias-primas farmacêuticas", on_delete=models.SET_NULL, null=True, blank=True)
  fuel = models.ForeignKey(Fuel, verbose_name="Detalhamento de combustível", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.description

  class Meta:
    verbose_name = 'Item'
    verbose_name_plural = 'Itens'

class Protocol(models.Model):
  protocol_id = models.AutoField(primary_key=True)
  id = models.CharField("Identificador da TAG a ser assinada, somente precisa ser informado se a UF assinar a resposta.", max_length=255, blank=True, null=False)
  environmentType = models.CharField("Identificação do Ambiente: 1 – Produção/2 - Homologação", max_length=15, blank=True, null=True)
  applicationVersion = models.CharField("Versão do Aplicativo que processou o Lote", max_length=255, blank=True, null=True)
  accessKey = models.CharField("Chave de Acesso da NF-e", max_length=44, blank=True, null=True)
  receiptOn = models.DateTimeField("Preenchido com a data e hora do processamento", blank=True, null=True)
  protocolNumber = models.CharField("Número do Protocolo da NF-e", max_length=255, blank=True, null=True)
  validatorDigit = models.CharField("(Digest Value) da NF-e processada Utilizado para conferir a integridade da NFe original.", max_length=255, blank=True, null=True)
  statusCode = models.IntegerField("Código do status da resposta para a NF-e", blank=True, null=True)
  description = models.TextField("Descrição literal do status da resposta para a NF-e", blank=True, null=True)
  signature = models.TextField("Assinatura XML do grupo identificado pelo atributo 'Id'", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.accessKey

  class Meta:
    verbose_name = 'Protocolo'
    verbose_name_plural = 'Protocolos'

class ReferencedProcess(models.Model):
  identifierConcessory = models.CharField("Concessão do Identificador", max_length=32, blank=True, null=True)
  identifierOrigin = models.IntegerField("Origem do Identificador", blank=True, null=True)

  class Meta:
    verbose_name = 'Processo Referenciado'
    verbose_name_plural = 'Processos Referenciados'

class TaxpayerComments(models.Model):
  field = models.CharField("Campo", max_length=255, blank=True, null=True)
  text = models.CharField("Texto", max_length=255, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Comentário do Contribuinte'
    verbose_name_plural = 'Comentários dos Contribuintes'

class DocumentInvoiceReference(models.Model):
  state = models.IntegerField("Estado", blank=True, null=True)
  yearMonth = models.CharField("Ano/mês", max_length=32, blank=True, null=True)
  federalTaxNumber = models.CharField("CNPJ do emitente/CPF do remetente", max_length=80, blank=True, null=True)
  model = models.CharField("Modelo", max_length=32, blank=True, null=True)
  series = models.CharField("Série", max_length=32, blank=True, null=True)
  number = models.CharField("Número", max_length=32, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Documento Fiscal de Referência'
    verbose_name_plural = 'Documentos Fiscais de Referência'

class TaxCouponInformation(models.Model):
  modelDocumentFiscal = models.CharField("Modelo do Documento Fiscal", max_length=32, blank=True, null=True)
  orderECF = models.CharField("Pedido ECF", max_length=32, blank=True, null=True)
  orderCountOperation = models.IntegerField("Operação de Contagem de Pedidos", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Informação sobre o Cupom Fiscal'
    verbose_name_plural = 'Informações sobre os Cupons Fiscais'

class TaxDocumentsReference(models.Model):
  taxCouponInformation = models.ForeignKey(TaxCouponInformation, verbose_name="Informação sobre o Cupom Fiscal", on_delete=models.SET_NULL, null=True, blank=True)
  documentInvoiceReference = models.ForeignKey(DocumentInvoiceReference, verbose_name="Documento Fiscal de Referencia", on_delete=models.SET_NULL, null=True, blank=True)
  accessKey = models.CharField("Chave de Acesso", max_length=120, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = "Taxa do Documento de Referência"
    verbose_name_plural = "Taxas dos Documentos de Referência"

class AdditionalInformation(models.Model):
  fisco = models.TextField("Informações Adicionais de Interesse do Fisco", blank=True, null=True)
  taxpayer = models.TextField("Informações Complementares de interesse do Contribuinte", blank=True, null=True)
  xmlAuthorized = models.TextField("Informações Complementares de interesse do Contribuinte", blank=True, null=True)
  effort = models.CharField(max_length=32, blank=True, null=True)
  order = models.CharField(max_length=32, blank=True, null=True)
  contract = models.CharField(max_length=32, blank=True, null=True)
  taxDocumentsReference = models.ManyToManyField(TaxDocumentsReference, verbose_name="Documentos Fiscais Referenciados", blank=True)
  taxpayerComments = models.ManyToManyField(TaxpayerComments, verbose_name="Grupo do campo de uso livre do contribuinte", blank=True)
  referencedProcess = models.ManyToManyField(ReferencedProcess, verbose_name="Grupo de Processos referenciados", blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return "Informação adicional %d criada em %s" % (self.id, self.created)

  class Meta:
    verbose_name = 'Informação Adicional'
    verbose_name_plural = 'Informações Adicionais'

class TransportRate(models.Model):
  serviceAmount = models.FloatField("Valor do Serviço", blank=True, null=True)
  bcRetentionAmount = models.FloatField("BC da Retenção do ICMS", blank=True, null=True)
  icmsRetentionRate = models.FloatField("Alíquota da Retenção", blank=True, null=True)
  icmsRetentionAmount = models.FloatField("Valor do ICMS Retido", blank=True, null=True)
  cfop = models.FloatField("CFOP de Serviço de Transporte", blank=True, null=True)
  cityGeneratorFactCode = models.FloatField("Código do Municipio de ocorrencia do fato gerador do ICMS do Transpote", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.serviceAmount)

  class Meta:
    verbose_name = 'Taxa de transporte'
    verbose_name_plural = 'Taxas de tansporte'

class TransportVehicle(models.Model):
  plate = models.CharField("Placa do Veiculo", max_length=25, blank=True, null=True)
  state = models.CharField("Sigla da UF", max_length=6, blank=True, null=True)
  rntc = models.CharField("Registro Nacional de Transportador de Carga (ANTT)", max_length=25, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.plate

  class Meta:
    verbose_name = 'Veículo transportador'
    verbose_name_plural = 'Veículos transportadores'

class TransportVolume(models.Model):
  volumeQuantity = models.IntegerField("Quantidade de volumes transportados", blank=True, null=True)
  species = models.CharField("Espécie dos volumes transportados", max_length=25, blank=True, null=True)
  brand = models.CharField("Marca dos Volumes Transportados", max_length=25, blank=True, null=True)
  volumeNumeration = models.CharField("Numeração dos Volumes Transportados", max_length=25, blank=True, null=True)
  netWeight = models.FloatField("Peso Liquido (em Kg)", blank=True, null=True)
  grossWeight = models.FloatField("Peso Bruto (em Kg)", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.species

  class Meta:
    verbose_name = "Volume transportado"
    verbose_name_plural = "Volumes transportados"

class TransportReboque(models.Model):
  plate = models.CharField("Placa do Veiculo", max_length=80, blank=True, null=True)
  uf = models.CharField("UF Veiculo Reboque", max_length=6, blank=True, null=True)
  rntc = models.CharField("Registro Nacional de Transportador de Carga (ANTT) (RNTC)", max_length=25, blank=True, null=True)
  wagon = models.CharField("Identificação do Vagão", max_length=32, blank=True, null=True)
  ferry = models.CharField("Identificação da Balsa", max_length=32, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.plate

  class Meta:
    verbose_name = "Reboque"
    verbose_name_plural = "Reboques"

class TransportGroup(models.Model):
  cityName = models.CharField("Nome do Município", max_length=80, blank=True, null=True)
  federalTaxNumber = models.CharField("CNPJ do Transportador (CNPJ) ou CPF do Transportador (CPF)", max_length=25, blank=True, null=True)
  cpf = models.CharField("CPF do Transportador (CPF)", max_length=11, blank=True, null=True)
  name = models.CharField("Razão Social ou nome", max_length=80, blank=True, null=True)
  stateTaxNumber = models.CharField("Inscrição Estadual do Transportador", max_length=25, blank=True, null=True)
  fullAddress = models.CharField("Endereço Completo", max_length=255, blank=True, null=True)
  state = models.CharField("Sigla da UF", max_length=10, blank=True, null=True)
  transportRetention = models.CharField("Grupo de Retenção do ICMS do transporte", max_length=50, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    if self.name:
      return self.name
    elif self.federalTaxNumber:
      return self.federalTaxNumber
    elif self.fullAddress:
      return self.fullAddress
    else:
      return "Transportadora id %d" % self.id

  class Meta:
    verbose_name = 'Transportadora'
    verbose_name_plural = 'Transportadoras'

class Transport(models.Model):
  freightModality = models.IntegerField('Modalidade do frete', blank=True, null=True)
  transportGroup = models.ForeignKey(TransportGroup, verbose_name="Grupo Transportador", on_delete=models.SET_NULL, null=True, blank=True)
  reboque = models.ForeignKey(TransportReboque, verbose_name="Grupo Reboque", on_delete=models.SET_NULL, null=True, blank=True)
  volume = models.ForeignKey(TransportVolume, verbose_name="Grupo de Volumes", on_delete=models.SET_NULL, null=True, blank=True)
  transportVehicle = models.ForeignKey(TransportVehicle, verbose_name="Grupo Veículo", on_delete=models.SET_NULL, null=True, blank=True)
  sealNumber = models.CharField("Número dos Lacres", max_length=25, blank=True, null=True)
  transpRate = models.ForeignKey(TransportRate, verbose_name="Grupo Retenção ICMS transporte", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.transportGroup.__str__()

  class Meta:
    verbose_name = 'Transporte'
    verbose_name_plural = 'Transportes'

class TotalsISSQN(models.Model):
  totalServiceNotTaxedICMS = models.FloatField("Valor Total Serv.Não Tributados p/ ICMS", blank=True, null=True)
  baseRateISS = models.FloatField("Base de Cálculo do ISS", blank=True, null=True)
  totalISS = models.FloatField("Valor Total do ISS", blank=True, null=True)
  valueServicePIS = models.FloatField("Valor do PIS sobre Serviços", blank=True, null=True)
  valueServiceCOFINS = models.FloatField("Valor da COFINS sobre Serviços", blank=True, null=True)
  provisionService = models.DateTimeField("Data Prestação Serviço", blank=True, null=True)
  deductionReductionBC = models.FloatField("Valor Dedução para Redução da BC", blank=True, null=True)
  valueOtherRetention = models.FloatField("Valor Outras Retenções", blank=True, null=True)
  discountUnconditional = models.FloatField("Valor Desconto Incondicionado", blank=True, null=True)
  discountConditioning = models.FloatField("Valor Desconto Condicionado", blank=True, null=True)
  totalRetentionISS = models.FloatField("Valor Total Retenção ISS", blank=True, null=True)
  codeTaxRegime = models.FloatField("Código Regime Tributação", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.totalISS

  class Meta:
    verbose_name = 'ISSQN Total'
    verbose_name_plural = 'ISSQN\'s Totais'

class TotalsICMS(models.Model):
  baseTax = models.FloatField("Base de Cálculo do ICMS", blank=True, null=True)
  icmsAmount = models.FloatField("Valor Total do ICMS", blank=True, null=True)
  icmsExemptAmount = models.FloatField("Valor ICMS Total desonerado", blank=True, null=True)
  stCalculationBasisAmount = models.FloatField("Base de Cálculo do ICMS Substituição Tributária", blank=True, null=True)
  stAmount = models.FloatField("Valor Total do ICMS ST ", blank=True, null=True)
  productAmount = models.FloatField("Valor Total dos produtos e serviços", blank=True, null=True)
  freightAmount = models.FloatField("Valor Total do Frete", blank=True, null=True)
  insuranceAmount = models.FloatField("Valor Total do Seguro", blank=True, null=True)
  invoiceAmount = models.FloatField("Valor Total da NF-e", blank=True, null=True)
  discountAmount = models.FloatField("Valor Total do Desconto", blank=True, null=True)
  iiAmount = models.FloatField("Valor Total do Imposto de Importação", blank=True, null=True)
  ipiAmount = models.FloatField("Valor Total do IPI", blank=True, null=True)
  pisAmount = models.FloatField("Valor do PIS", blank=True, null=True)
  cofinsAmount = models.FloatField("Valor do COFINS", blank=True, null=True)
  othersAmount = models.FloatField("Outras Despesas acessórias", blank=True, null=True)
  fcpufDestinationAmount = models.FloatField("Valor Total da NF-e", blank=True, null=True)
  icmsufDestinationAmount = models.FloatField("Valor Total ICMS FCP UF Destino", blank=True, null=True)
  icmsufSenderAmount = models.FloatField("Valor Total ICMS Interestadual UF Destino", blank=True, null=True)
  federalTaxesAmount = models.FloatField("Valor aproximado total de tributos federais, estaduais e municipais.", blank=True, null=True)
  fcpAmount = models.FloatField("Valor Total do FCP - Valor do ICMS relativo ao Fundo de Combate à Pobreza", blank=True, null=True)
  fcpstAmount = models.FloatField("Valor Total do FCP retido por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (vFCP) retido por substituição tributária.", blank=True, null=True)
  fcpstRetAmount = models.FloatField("Valor Total do FCP retido por anteriormente por ST - Valor do ICMS relativo ao Fundo de Combate à Pobreza (vFCP) retido anteriormente por substituição tributária.", blank=True, null=True)
  ipiDevolAmount = models.FloatField("Valor total do IPI devolvido", blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.baseTax)

  class Meta:
    verbose_name = 'ICMS Total'
    verbose_name_plural = 'ICMS\'s Totais'

class Totals(models.Model):
  icms = models.ForeignKey(TotalsICMS, verbose_name="ICMS Total", on_delete=models.SET_NULL, null=True, blank=True)
  issqn = models.ForeignKey(TotalsISSQN, verbose_name="ICMS Total", on_delete=models.SET_NULL, null=True, blank=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return str(self.icms.baseTax)

  class Meta:
    verbose_name = 'Imposto total'
    verbose_name_plural = 'Impostos totais'

class Buyer(models.Model):
  federalTaxNumber = models.CharField("Identificação do destinatário (CPF, CNPJ, idEstrangeiro)", max_length=25, blank=True, null=True)
  name = models.CharField("Razão Social ou nome do destinatário", max_length=120, blank=True, null=True)
  address = models.ForeignKey(Address, verbose_name='Endereço', on_delete=models.SET_NULL, null=True, blank=True)
  stateTaxNumber = models.CharField("Inscrição Estadual", max_length=25, blank=True, null=True)
  stateTaxNumberIndicator = models.IntegerField("Indicador Inscrição Estadual", blank=True, null=True)
  email = models.CharField("E-mail", max_length=120, blank=True, null=True)
  type = models.CharField("Tipo da pessoa: Jurídica ou Física", max_length=25, blank=True, null=True)

  def __str__(self):
    if self.name:
      return self.name
    else:
      return ''

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  class Meta:
    verbose_name = 'Comprador'
    verbose_name_plural = 'Compradores'

class Issuer(models.Model):
  federalTaxNumber = models.CharField('CNPJ do emitente / CPF do remetente', max_length=25, blank=True, null=True)
  name = models.CharField('Razão Social ou Nome do emitente', max_length=120, blank=True, null=True)
  tradeName = models.CharField('Nome fantasia', max_length=120, blank=True, null=True)
  address = models.ForeignKey(Address, verbose_name="Endereço", on_delete=models.SET_NULL, null=True, blank=True)
  stateTaxNumber = models.CharField('Inscrição Estadual', max_length=25, blank=True, null=True)
  codeTaxRegime = models.CharField('Código de Regime Tributário', max_length=25, blank=True, null=True)
  cnae = models.IntegerField('CNAE fiscal', blank=True, null=True)
  im = models.CharField('Inscrição Municipal do Prestador de Serviço', max_length=25, blank=True, null=True)
  iest = models.CharField('IE do Substituto Tributário', max_length=25, blank=True, null=True)
  type = models.CharField('Tipo da pessoa: Jurídica ou Física', max_length=25, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Emissor'
    verbose_name_plural = 'Emissores'

class Invoice(models.Model):
  currentStatus = models.CharField("Situação Atual", max_length=120, blank=True, null=True)
  stateCode = models.FloatField("Código da UF do emitente do Documento Fiscal", blank=True, null=True)
  checkCode = models.FloatField("Código Numérico que compõe a Chave de Acesso", blank=True, null=True)
  operationNature = models.CharField("Descrição da Natureza da Operação", max_length=120, blank=True, null=True)
  paymentType = models.CharField("Indicador da forma de pagamento", max_length=120, blank=True, null=True)
  codeModel = models.FloatField("Código do Modelo do Documento Fiscal", blank=True, null=True)
  serie = models.FloatField("Série do Documento Fiscal", blank=True, null=True)
  number = models.FloatField("Número do Documento Fiscal", blank=True, null=True)
  issuedOn = models.DateTimeField("Data de emissão do Documento Fiscal", blank=True, null=True)
  operationOn = models.DateTimeField("Data e Hora de Saída ou da Entrada da Mercadoria/Produto", blank=True, null=True)
  operationType = models.CharField("Tipo de Operação", max_length=120, blank=True, null=True)
  destination = models.CharField("Identificador de local de destino da operação", max_length=120, blank=True, null=True)
  cityCode = models.FloatField("Código do Município de Ocorrência do Fato Gerador", blank=True, null=True)
  printType = models.CharField("Formato de Impressão do DANFE", max_length=120, blank=True, null=True)
  issueType = models.CharField("Tipo de Emissão da NF-e", max_length=120, blank=True, null=True)
  checkCodeDigit = models.FloatField("Dígito Verificador da Chave de Acesso da NF-e", blank=True, null=True)
  environmentType = models.CharField("Identificação do Ambiente", max_length=120, blank=True, null=True)
  purposeType = models.CharField("Finalidade de emissão da NF-e", max_length=120, blank=True, null=True)
  consumerType = models.CharField("Indica operação com Consumidor final", max_length=120, blank=True, null=True)
  presenceType = models.CharField("Indicador de presença do comprador no estabelecimento comercial no momento da operação", max_length=120, blank=True, null=True)
  processType = models.CharField("Processo de emissão da NF-e", max_length=120, blank=True, null=True)
  invoiceVersion = models.CharField("Versão do Processo de emissão da NF-e", max_length=120, blank=True, null=True)
  xmlVersion = models.CharField("Versão do leiaute", max_length=120, blank=True, null=True)
  contingencyOn = models.DateTimeField("Data e Hora da entrada em contingência", blank=True, null=True)
  contingencyJustification = models.CharField("Justificativa da entrada em contingência", max_length=120, blank=True, null=True)
  issuer = models.ForeignKey(Issuer, verbose_name="Fornecedor", on_delete=models.SET_NULL, null=True, blank=True)
  buyer = models.ForeignKey(Buyer, verbose_name="Grupo de identificação do Destinatário da NF-e", on_delete=models.SET_NULL, null=True, blank=True)
  totals = models.ForeignKey(Totals, verbose_name="Grupo Totais da NF-e ", on_delete=models.SET_NULL, null=True, blank=True)
  transport = models.ForeignKey(Transport, verbose_name="Grupo de Informações do Transporte da NF-e", on_delete=models.SET_NULL, null=True, blank=True)
  additionalInformation = models.ForeignKey(AdditionalInformation, verbose_name="Informacoes Adicionais", on_delete=models.SET_NULL, null=True, blank=True)
  protocol = models.ForeignKey(Protocol, verbose_name="Informações do Protocolo de resposta. TAG a ser assinada", on_delete=models.CASCADE, null=True, blank=True)
  items = models.ManyToManyField(Item, verbose_name="Grupo do detalhamento de Produtos e Serviços da NF-e", blank=True)
  billing = models.ForeignKey(Billing, verbose_name="Grupo Cobrança", on_delete=models.SET_NULL, null=True, blank=True)
  payment = models.ManyToManyField(Payment, verbose_name="Formas de Pagamento", blank=True)

  type = models.CharField("Tipo de Nota Fiscal", max_length=25, blank=True, null=True)
  isPending = models.BooleanField('Pendente', default=True, blank=True, null=True)

  # Meta Fields
  created = models.DateTimeField("Criado em", auto_now_add=True)
  updated = models.DateTimeField("Atualizado em", auto_now=True)

  def __str__(self):
    return _("Nota nº %d, série %d, criada em %s.") % (self.number, self.serie, naturaltime(self.created))

  class Meta:
    verbose_name = 'Nota Fiscal Eletrônica'
    verbose_name_plural = 'Notas Fiscais Eletrônicas'
