from .models import Brand
from .serializers import BrandSerializer
from rest_framework import routers, serializers, viewsets

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
