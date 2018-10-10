from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import VehicleKind
from .serializers import VehicleKindSerializer
from django.shortcuts import render

# Create your views here.
class VehicleKindTask(APIView):

    def get(self, request, format=None):
        id_ = request.GET.get('id')
        if id_:
            vehicleKind = VehicleKind.objects.get(id=id_)
        else:
            vehicleKinds = VehicleKind.objects.all()
            serializer = VehicleKindSerializer(vehicleKinds, many=True)
            return Response(serializer.data)

        if vehicleKind:
            serializer = VehicleKindSerializer(vehicleKind)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)