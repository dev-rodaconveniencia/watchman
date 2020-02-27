from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from . import models

class CitySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.City
    fields = '__all__'

class AddressSerializer(WritableNestedModelSerializer):
  city = CitySerializer(many=False, required=False)

  class Meta:
    model = models.Address
    fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Card
    fields = '__all__'

class PaymentDetailSerializer(WritableNestedModelSerializer):
  card = CardSerializer(many=False, required=False)

  class Meta:
    model = models.PaymentDetail
    fields = '__all__'

class PaymentSerializer(WritableNestedModelSerializer):
  paymentDetail = PaymentDetailSerializer(many=True, required=False)

  class Meta:
    model = models.Payment
    fields = '__all__'

class DuplicatesSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Duplicates
    fields = '__all__'

class BillSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Bill
    fields = '__all__'

class BillingSerializer(WritableNestedModelSerializer):
  bill = BillSerializer(many=False, required=False)
  duplicates = DuplicatesSerializer(many=True, required=False)

  class Meta:
    model = models.Billing
    fields = '__all__'

class FuelPumpSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.FuelPump
    fields = '__all__'

class FuelCideSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.FuelCide
    fields = '__all__'

class FuelSerializer(WritableNestedModelSerializer):
  cide = FuelCideSerializer(many=False, required=False)
  pump = FuelPumpSerializer(many=False, required=False)

  class Meta:
    model = models.Fuel
    fields = '__all__'

class MedicineDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.MedicineDetail
    fields = '__all__'

class TaxICMSDestinationSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxICMSDestination
    fields = '__all__'

class TaxCOFINSSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxCOFINS
    fields = '__all__'

class TaxPISSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxPIS
    fields = '__all__'

class TaxIISerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxII
    fields = '__all__'

class TaxIPISerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxIPI
    fields = '__all__'

class TaxICMSSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxICMS
    fields = '__all__'

class TaxSerializer(WritableNestedModelSerializer):
  icms = TaxICMSSerializer(many=False, required=False)
  ipi = TaxIPISerializer(many=False, required=False)
  ii = TaxIISerializer(many=False, required=False)
  pis = TaxPISSerializer(many=False, required=False)
  cofins = TaxCOFINSSerializer(many=False, required=False)
  icmsDestination = TaxICMSDestinationSerializer(many=False, required=False)

  class Meta:
    model = models.Tax
    fields = '__all__'

class ItemsSerializer(WritableNestedModelSerializer):
  id = serializers.IntegerField(read_only=True)
  tax = TaxSerializer(many=False, required=False)
  medicineDetail = MedicineDetailSerializer(many=False, required=False)
  fuel = FuelSerializer(many=False, required=False)

  def validate_description(self, description):
    description = description.upper()
    return description

  def validate_codeGTIN(self, codeGTIN):
    if not codeGTIN.isdigit():
      codeGTIN = None
    return codeGTIN

  class Meta:
    model = models.Item
    fields = '__all__'

class ProtocolSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Protocol
    fields = '__all__'

class ReferencedProcessSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.ReferencedProcess
    fields = '__all__'

class TaxpayerCommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxpayerComments
    fields = '__all__'

class DocumentInvoiceReferenceSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.DocumentInvoiceReference
    fields = '__all__'

class TaxCouponInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TaxCouponInformation
    fields = '__all__'

class TaxDocumentsReferenceSerializer(WritableNestedModelSerializer):
  taxCouponInformation = TaxCouponInformationSerializer(many=False, required=False)
  documentInvoiceReference = DocumentInvoiceReferenceSerializer(many=False, required=False)

  class Meta:
    model = models.TaxDocumentsReference
    fields = '__all__'

class AdditionalInformationSerializer(WritableNestedModelSerializer):
  taxDocumentsReference = TaxDocumentsReferenceSerializer(many=True, required=False)
  taxpayerComments = TaxpayerCommentsSerializer(many=True, required=False)
  referencedProcess = ReferencedProcessSerializer(many=True, required=False)
  xmlAuthorized = serializers.JSONField(required=False)

  class Meta:
    model = models.AdditionalInformation
    fields = '__all__'

class TransportRateSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransportRate
    fields = '__all__'

class TransportVehicleSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransportVehicle
    fields = '__all__'

class TransportVolumeSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransportVolume
    fields = '__all__'

class TransportReboqueSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransportReboque
    fields = '__all__'

class TransportGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TransportGroup
    fields = '__all__'

class TransportSerializer(WritableNestedModelSerializer):
  transportGroup = TransportGroupSerializer(many=False, required=False)
  reboque = TransportReboqueSerializer(many=False, required=False)
  volume = TransportVolumeSerializer(many=False, required=False)
  transportVehicle = TransportVehicleSerializer(many=False, required=False)
  transpRate = TransportRateSerializer(many=False, required=False)

  class Meta:
    model = models.Transport
    fields = '__all__'

class TotalsISSQNSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TotalsISSQN
    fields = '__all__'

class TotalsICMSSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.TotalsICMS
    fields = '__all__'

class TotalsSerializer(WritableNestedModelSerializer):
  icms = TotalsICMSSerializer(many=False, required=False)
  issqn = TotalsISSQNSerializer(many=False, required=False)

  class Meta:
    model = models.Totals
    fields = '__all__'

class BuyerSerializer(WritableNestedModelSerializer):
  address = AddressSerializer(many=False, required=False)

  class Meta:
    model = models.Buyer
    fields = '__all__'

class IssuerSerializer(WritableNestedModelSerializer):
  address = AddressSerializer(many=False, required=False)

  class Meta:
    model = models.Issuer
    fields = '__all__'

class InvoiceSerializer(WritableNestedModelSerializer):
  issuer = IssuerSerializer(many=False, required=False)
  buyer = BuyerSerializer(many=False, required=False)
  totals = TotalsSerializer(many=False, required=False)
  transport = TransportSerializer(many=False, required=False)
  additionalInformation = AdditionalInformationSerializer(many=False, required=False)
  protocol = ProtocolSerializer(many=False, required=False)
  items = ItemsSerializer(many=True, required=False)
  billing = BillingSerializer(many=False, required=False)
  payment = PaymentSerializer(many=True, required=False)

  class Meta:
    model = models.Invoice
    fields = '__all__'
