from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, schema
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import list_route

from django.http import Http404
from .models import Vehicle
from brand.models import Brand
from .serializers import VehicleSerializer,VehicleDTOForm
from brand.serializers import BrandSerializer

class VehicleTask(APIView):

    def get(self, request, format=None):
        id_ = request.GET.get('id')
        brand_ = request.GET.get('brand')      
        try:
            if id_:
                vehicle = Vehicle.objects.get(id=id_)
            elif brand_:
                vehicles = Vehicle.objects.filter(brand_id=brand_)
                serializer = VehicleSerializer(vehicles, many=True)
                return Response(serializer.data)
            else:
                vehicles = Vehicle.objects.all()
                serializer = VehicleSerializer(vehicles, many=True)
                return Response(serializer.data)

            if vehicle:
                serializer = VehicleSerializer(vehicle)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, format=None):
    #     id = request.GET.get('id')
    #     vehicle = Vehicle.objects.get(id=id)
    #     print(vehicle)
    #     if vehicle:
    #         serializer = VehicleSerializer(vehicle, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        try:
           
            id=request.data.get('vehicle').get('id')
           
            enrollment=request.data.get('enrollment')
           
            city_id=request.data.get('vehicle').get('city')
           
            response_data = None
            print(request.data)
            if id is not None:
                print('not none')
                vehicle = Vehicle.objects.get(id=id)
                print(vehicle)
                if vehicle:
                    print('vehicle ok')
                    serializer = VehicleSerializer(vehicle, data=request.data)
                    if serializer.is_valid():
                        print('serializer valid')
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
            else:
                print('else')
                vehicle = Vehicle.objects.filter(enrollment=enrollment,city_id=city_id).first()
                print(vehicle)
                if vehicle is None:
                    print('none')
                    serializer = VehicleSerializer(data=request.data)
                    if serializer.is_valid():
                        print('valid')
                        serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    response_data={
                        "state":False,
                        "message":"La matrícula para la ciudad ya se encuentra registrada"
                    }
                    return Response(response_data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def delete(self, request, format=None):
    #     name = request.GET.get('name')
    #     animal = Animal.objects.get(name=name)
    #     if animal:
    #         animal.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)