from django.contrib import admin
from . import models

@admin.register(models.Address)
class Address(admin.ModelAdmin):
  pass

@admin.register(models.Checkout)
class Checkout(admin.ModelAdmin):
  pass

@admin.register(models.Instalation)
class Instalation(admin.ModelAdmin):
  pass
