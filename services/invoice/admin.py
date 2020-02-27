from django.utils.safestring import mark_safe
from django.contrib import admin
from . import models

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
  pass

@admin.register(models.PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Duplicates)
class DuplicatesAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Billing)
class BillingAdmin(admin.ModelAdmin):
  pass

@admin.register(models.FuelPump)
class FuelPumpAdmin(admin.ModelAdmin):
  pass

@admin.register(models.FuelCide)
class FuelCideAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Fuel)
class FuelAdmin(admin.ModelAdmin):
  pass

@admin.register(models.MedicineDetail)
class MedicineDetailAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxICMSDestination)
class TaxICMSDestinationAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxCOFINS)
class TaxCOFINSAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxPIS)
class TaxPISAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxII)
class TaxIIAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxIPI)
class TaxIPIAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxICMS)
class TaxICMSAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Tax)
class TaxAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Protocol)
class ProtocolAdmin(admin.ModelAdmin):
  pass

@admin.register(models.ReferencedProcess)
class ReferencedProcessAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxpayerComments)
class TaxpayerCommentsAdmin(admin.ModelAdmin):
  pass

@admin.register(models.DocumentInvoiceReference)
class DocumentInvoiceReferenceAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxCouponInformation)
class TaxCouponInformationAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TaxDocumentsReference)
class TaxDocumentsReferenceAdmin(admin.ModelAdmin):
  pass

@admin.register(models.AdditionalInformation)
class AdditionalInformationAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TransportRate)
class TransportRateAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TransportVehicle)
class TransportVehicleAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TransportVolume)
class TransportVolumeAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TransportReboque)
class TransportReboqueAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TransportGroup)
class TransportGroupAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Transport)
class TransportAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TotalsISSQN)
class TotalsISSQNAdmin(admin.ModelAdmin):
  pass

@admin.register(models.TotalsICMS)
class TotalsICMSAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Totals)
class TotalsAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Issuer)
class IssuerAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Invoice)
class InvoiceAdmin(admin.ModelAdmin):
  list_display = ['number', 'issuer', 'created']
  search_fields = ['products__description']
