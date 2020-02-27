from django.contrib import admin
from . import models

@admin.register(models.Overman)
class Overman(admin.ModelAdmin):
  pass
