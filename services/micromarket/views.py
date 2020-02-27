from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated

from . import serializers
from . import models
from services.manager.models import User

@api_view(['GET'])
@permission_classes([AllowAny])
def _ask_for_authentication(request):
  macaddress = request.query_params.get("macaddress")
  email = "%s@rodaconveniencia.com.br" % macaddress
  user = User.objects.filter(email=email)
  isRegistered = user.count() != 0
  context = dict(isregistered=isRegistered, user=user.values())
  return Response(context)

class AddressViewSet(viewsets.ModelViewSet):
  queryset = models.Address.objects.all()
  serializer_class = serializers.AddressSerializer
  filter_backends = [DjangoFilterBackend]

class CheckoutViewSet(viewsets.ModelViewSet):
  queryset = models.Checkout.objects.all()
  serializer_class = serializers.CheckoutSerializer
  filter_backends = [DjangoFilterBackend]

  @action(detail=False, methods=['post'], url_path="new/sale")
  def _new_sale(self, request):
    return Response({})

class InstalationViewSet(viewsets.ModelViewSet):
  queryset = models.Instalation.objects.all()
  serializer_class = serializers.InstalationSerializer
  filter_backends = [DjangoFilterBackend]
