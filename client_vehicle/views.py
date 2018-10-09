from .models import ClientVehicle
from .serializers import ClientVehicleSerializer
from rest_framework import routers, serializers, viewsets

class ClientVehicleViewSet(viewsets.ModelViewSet):
    queryset = ClientVehicle.objects.all()
    serializer_class = ClientVehicleSerializer
