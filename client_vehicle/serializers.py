from rest_framework import serializers
from .models import ClientVehicle

from state.serializers import StateSerializer
from client.serializers import ClientSerializer
from vehicle.serializers import VehicleSerializer

class ClientVehicleSerializer(serializers.ModelSerializer):
    state = StateSerializer()
    vehicle = VehicleSerializer()
    client = ClientSerializer()

    class Meta:
        model = ClientVehicle
        fields = ('id', 'vehicle','client','state')