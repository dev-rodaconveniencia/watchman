from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin
from rest_framework.permissions import AllowAny

from rest_framework import serializers
from . import models

from services.wharehouse import serializers as wharehouse

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Address
    fields = '__all__'

class CheckoutSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  capex = wharehouse.CapexSerializer(many=True)

  class Meta:
    model = models.Checkout
    fields = '__all__'

class InstalationSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  checkout = CheckoutSerializer(many=False)
  capex = wharehouse.CapexSerializer(many=True)
  address = AddressSerializer(many=False)

  class Meta:
    model = models.Instalation
    fields = '__all__'
