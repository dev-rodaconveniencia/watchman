from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin
from rest_framework import serializers
from . import models

class CapexTypeSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  class Meta:
    model = models.CapexType
    fields = '__all__'

class CapexSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  type = CapexTypeSerializer(many=False)

  class Meta:
    model = models.Capex
    fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Product
    fields = '__all__'

class PicklistProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.PicklistProduct
    fields = '__all__'

class PicklistSerializer(serializers.ModelSerializer):    
  class Meta:
    model = models.Picklist
    fields = '__all__'

class PlanogramProductDiscountSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  products = ProductSerializer(many=False)

  class Meta:
    model = models.PlanogramProductDiscount
    fields = '__all__'

class PlanogramProductSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  product = ProductSerializer(many=False)
  discount = PlanogramProductDiscountSerializer(many=False)

  class Meta:
    model = models.PlanogramProduct
    fields = '__all__'

class PlanogramSerializer(serializers.ModelSerializer):
  products = PlanogramProductSerializer(many=True)

  class Meta:
    model = models.Planogram
    fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Sale
    fields = '__all__'
