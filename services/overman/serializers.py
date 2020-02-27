from drf_writable_nested.serializers import WritableNestedModelSerializer, NestedUpdateMixin
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_framework import serializers
from . import models

from services.micromarket import serializers as micromarket

class OvermanSerializer(NestedUpdateMixin, serializers.ModelSerializer):
  instalation = micromarket.InstalationSerializer(many=False)
  ddmmyyy_created = serializers.DateTimeField(format="%d/%m/%Y", read_only=True, source="created")
  natural_created = serializers.SerializerMethodField()
  is_solved = serializers.SerializerMethodField(read_only=True)

  def get_is_solved(self, object):
    if (object.isChecked):
      return "isChecked"
    else:
      return ""

  def get_natural_created(self, object):
    natural = naturaltime(object.created)
    if "agora" in natural:
      return natural.title()
    return "Há %s" % natural

  class Meta:
    model = models.Overman
    fields = '__all__'
