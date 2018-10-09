from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from .serializers import VehicleSerializer,UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'vehicles', views.VehicleViewSet)
#router.register(r'vehicle', views.vehicle_list)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]