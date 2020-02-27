from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets

from . import models
from . import serializers

class OvermanViewSet(viewsets.ModelViewSet):
  queryset = models.Overman.objects.all().order_by("-created")
  serializer_class = serializers.OvermanSerializer
  filter_backends = [DjangoFilterBackend]
  filter_fields = {
    "id": ["exact"],
    "reference": ["exact", "contains"],
    "isChecked": ["exact"],
    "level": ["exact"],
    "ddmmyyy_created": ["exact"]
  }

  def get_paginated_response(self, data):
    return Response(data)
