from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, schema
from rest_framework import routers, serializers, viewsets
from rest_framework.decorators import list_route

from .models import ClientVehicle
from vehicle.models import Vehicle
from .serializers import ClientVehicleSerializer, ClientVehicleDTOForm



class ClientVehicleTask(APIView):
    def get(self, request, format=None):
        id_ = request.GET.get("id")
        client_ = request.GET.get("client")
        vehicle_ = request.GET.get("vehicle")
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


@api_view(["POST"])
def manageVehicleEnroll(request):
    try:
        form_data = ClientVehicleDTOForm(data=request.data)
        response_data = None
        if form_data.is_valid():
            city_id = form_data.data.get("vehicle").get("city")
            brand_id = form_data.data.get("vehicle").get("brand")
            kind_id = form_data.data.get("vehicle").get("kind")
            enrollment = form_data.data.get("vehicle").get("enrollment")
            client_id = form_data.data.get("client").get("id")
            vehicle = Vehicle.objects.filter(enrollment=enrollment, city_id=city_id)
            if vehicle.count() < 1:
                vehicle = Vehicle(
                    enrollment=enrollment,
                    city_id=city_id,
                    brand_id=brand_id,
                    kind_id=kind_id,
                )
                vehicle.save()
                vehicle_id = vehicle.id
                client_vehicle = ClientVehicle(
                    client_id=client_id, vehicle_id=vehicle_id
                )
                client_vehicle.save()
                response_data = {
                    "state": True,
                    "message": "Vehículo creado y vinculado correctamente",
                }
            else:
                response_data = {
                    "state": False,
                    "message": "El vehículo ya se encuentra registrado",
                }
                return Response(response_data, status=status.HTTP_202_ACCEPTED)
                response_data = form_data.data
        else:
            response_data = {"state": False, "message": "Faltan datos por registrar"}
        return Response(response_data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status=status.HTTP_204_NO_CONTENT)


