from django.contrib import admin

from . import models
from services.invoice import models as invoice

@admin.register(models.CapexType)
class CapexTypeAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Capex)
class CapexAdmin(admin.ModelAdmin):
  pass

class InvoiceInline(admin.TabularInline):
  model = models.Product.invoices.through
  verbose_name = 'Nota Fiscal'
  verbose_name_plural = 'Notas Fiscais'

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  ordering = ['description']
  search_fields = ['description']
  inlines = [InvoiceInline]
  exclude = ['invoices']

@admin.register(models.Expiration)
class ExpirationAdmin(admin.ModelAdmin):
  pass

@admin.register(models.PicklistProduct)
class PicklistProductAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Picklist)
class PicklistAdmin(admin.ModelAdmin):
  pass

@admin.register(models.PlanogramProductDiscount)
class PlanogramProductDiscountAdmin(admin.ModelAdmin):
  pass

@admin.register(models.PlanogramProduct)
class PlanogramProductAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Planogram)
class PlanogramAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Billet)
class BilletAdmin(admin.ModelAdmin):
  pass
