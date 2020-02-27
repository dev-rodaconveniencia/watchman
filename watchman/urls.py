from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers

import services.invoice.views as invoice
import services.wharehouse.views as wharehouse
import services.overman.views as overman
import services.micromarket.views as micromarket

router = routers.DefaultRouter(trailing_slash=True)

# Overman router
router.register('overman/inspector', overman.OvermanViewSet)
# Invoice router
router.register('invoice', invoice.InvoiceViewSet)
router.register('invoice-items', invoice.ItemViewSet)
# Wharehouse router
router.register('wharehouse/products', wharehouse.ProductViewSet)
router.register('wharehouse/planogram', wharehouse.PlanogramViewSet)
router.register('wharehouse/picklist', wharehouse.PicklistViewSet)
router.register('wharehouse/capex/type', wharehouse.CapexTypeViewSet)
# Micromarket router
router.register('micromarket/checkout', micromarket.CheckoutViewSet)
router.register('micromarket/installation', micromarket.InstalationViewSet)

urlpatterns = [
  # Django admin
  path('admin/', admin.site.urls),
  # Django Rest Framwork Router
  url(r'api/v1/', include(router.urls)),
  url(r'^auth/', include('djoser.urls')),
  path('api/v1/auth/', include('djoser.urls.authtoken')),
  # Public ways
  path('ask_for_authentication/', micromarket._ask_for_authentication, name='ask-for-authentication'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
