from rest_framework import serializers
from .models import ClientVehicle

from django import forms

from state.serializers import StateSerializer
from client.serializers import ClientSerializer
from vehicle.serializers import VehicleSerializer,VehicleDTOForm


class ClientVehicleSerializer(serializers.ModelSerializer):
    state = StateSerializer()
    vehicle = VehicleSerializer()
    client = ClientSerializer()

    class Meta:
        model = ClientVehicle
        fields = ('id', 'vehicle','client','state')

class ClientVehicleDTOForm(forms.Form):
    client = ClientSerializer()
    vehicle = VehicleDTOForm()
