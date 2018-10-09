from rest_framework import serializers
from .models import Client
from state.serializers import StateSerializer

class ClientSerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = Client
        fields = ('id', 'email','identification','scanned_identification','first_name','last_name','modified','state')