"""carsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from client import views as clientView
from client_vehicle import views as clientVehicleView
from city import views as cityView
from vehicle import views as vehicleView
from vehicle_kind import views as vehicleKindView
from . import views as localViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'$', localViews.home_page),
    url(r'^', include('brand.urls')),
    url(r'^vehicle/$', vehicleView.VehicleTask.as_view()),
    url(r'^manageVehicle/', include('vehicle.urls')),
    url(r'^client/$', clientView.ClientTask.as_view()),
    url(r'^clientVehicle/$', clientVehicleView.ClientVehicleTask.as_view()),    
    url(r'^city/$', cityView.CityTask.as_view()),
    url(r'^kind/$', vehicleKindView.VehicleKindTask.as_view()),
    url(r'^manageVehicle/', include('client_vehicle.urls')),
    url(r'^', include('state.urls')),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns