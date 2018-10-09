from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# from rest_framework import routers

# router = routers.DefaultRouter()

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    url(r'^brand/$', views.brand_list),
    url(r'^brand/(?P<pk>[0-9]+)/$', views.brand_detail),
]

urlpatterns =format_suffix_patterns(urlpatterns)
