from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^vehicle/$', views.vehicle_list),
    url(r'^vehicle/(?P<pk>[0-9]+)/$', views.vehicle_detail),
]

urlpatterns =format_suffix_patterns(urlpatterns)
