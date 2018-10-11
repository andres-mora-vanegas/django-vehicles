from rest_framework import serializers
from brand.models import Brand

from state.serializers import StateSerializer

class BrandSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Brand
        fields = ('id', 'name','image','created','modified','state')