from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):    

    class Meta:
        model = Country
        #read_only_fields = ('id', 'brands')
        fields = ('id', 'name','created','modified','state')
        #fields = "__all__"