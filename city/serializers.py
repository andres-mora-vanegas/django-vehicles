from rest_framework import serializers
from .models import City
from country.serializers import CountrySerializer


class CitySerializer(serializers.ModelSerializer):
    country=CountrySerializer();

    class Meta:
        model = City
        #read_only_fields = ('id', 'brands')
        fields = ('id', 'name','country','created','modified','state')
        #fields = "__all__"