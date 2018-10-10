from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import City
from .serializers import CitySerializer
from django.shortcuts import render

# Create your views here.
class CityTask(APIView):

    def get(self, request, format=None):
        id_ = request.GET.get('id')
        if id_:
            city = City.objects.get(id=id_)
        else:
            citys = City.objects.all()
            serializer = CitySerializer(citys, many=True)
            return Response(serializer.data)

        if city:
            serializer = CitySerializer(city)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)