from rest_framework import serializers
from .models import Vehicle
from brand.serializers import BrandSerializer
from vehicle_kind.serializers import VehicleKindSerializer

class VehicleSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    kind = VehicleKindSerializer()
    #brands = serializers.StringRelatedField(many=True)
    #brands = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Vehicle
        #read_only_fields = ('id', 'brands')
        fields = ('id', 'enrollment','city','brand','kind','created','modified','state')
        #fields = "__all__"