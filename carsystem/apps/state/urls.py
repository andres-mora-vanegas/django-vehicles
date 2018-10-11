from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'states', views.StateViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]