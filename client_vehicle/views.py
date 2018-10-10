from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ClientVehicle
from .serializers import ClientVehicleSerializer
from rest_framework import routers, serializers, viewsets

class ClientVehicleTask(APIView):   
    
    def get(self, request, format=None):
        id_ = request.GET.get('id')
        client_ = request.GET.get('client')
        vehicle_ = request.GET.get('vehicle')
        clientVehicle = None
        try:
            if id_:
                clientVehicle = ClientVehicle.objects.get(id=id_)
            elif client_:
                clientVehicles = ClientVehicle.objects.filter(client_id=client_)
            elif vehicle_:
                clientVehicles = ClientVehicle.objects.filter(vehicle_id=vehicle_)
            else:
                clientVehicles = ClientVehicle.objects.all()            

            if clientVehicle is not None:
                serializer = ClientVehicleSerializer(clientVehicle)
                return Response(serializer.data)
            elif clientVehicles:
                serializer = ClientVehicleSerializer(clientVehicles, many=True)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)        
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

    
       

    # def put(self, request, format=None):
    #     name = request.GET.get('name')
    #     animal = Animal.objects.get(name=name)
    #     if animal:
    #         serializer = ClientSerializer(animal, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        
        # state = State(id=1,name='activo')
        # state.save()
        # print(state)
        # request.data.state=state
        # print(request.data)
        # print('before override')
        serializer = ClientVehicleSerializer(data=request.data)
        # print('override')
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    # def delete(self, request, format=None):
    #     name = request.GET.get('name')
    #     animal = Animal.objects.get(name=name)
    #     if animal:
    #         animal.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)