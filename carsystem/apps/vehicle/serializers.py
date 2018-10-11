from rest_framework import serializers
from django import forms

from .models import Vehicle
from brand.serializers import BrandSerializer
from city.serializers import CitySerializer
from vehicle_kind.serializers import VehicleKindSerializer

from django.contrib.auth.models import User

class VehicleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    kind = VehicleKindSerializer()
    city = CitySerializer()

    class Meta:
        model = Vehicle
        # read_only_fields = ('created', 'modified','state')
        fields = ('id', 'enrollment','city','brand','kind','created','modified','state')

class VehicleDTOForm(forms.Form):
    enrollment = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    kind = forms.CharField(max_length=100)
        

