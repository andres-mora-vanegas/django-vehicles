from rest_framework import serializers
from .models import Vehicle
from brand.serializers import BrandSerializer
from city.serializers import CitySerializer
from vehicle_kind.serializers import VehicleKindSerializer

from django.contrib.auth.models import User

class VehicleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    kind = VehicleKindSerializer()
    city = CitySerializer()
    #brands = serializers.StringRelatedField(many=True)
    #brands = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Vehicle
        #read_only_fields = ('id', 'brands')
        fields = ('id', 'enrollment','city','brand','kind','created','modified','state')
        #fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')