from rest_framework import serializers
from .models import VehicleKind

class VehicleKindSerializer(serializers.ModelSerializer):
    #brands = serializers.StringRelatedField(many=True)
    #brands = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = VehicleKind
        fields = ('name', 'image')