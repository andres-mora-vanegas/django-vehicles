from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Client
from .serializers import ClientSerializer

class ClientTask(APIView):

    def get(self, request, format=None):
        id_ = request.GET.get('id')
        if id_:
            client = Client.objects.get(id=id_)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)

        if client:
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # def put(self, request, format=None):
    #     id = request.GET.get('id')
    #     client = Client.objects.get(id=id)
    #     print(client)
    #     if client:
    #         serializer = ClientSerializer(client, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        try:
            id=request.data.get('id')
            identification=request.data.get('identification')
            response_data = None            
            if id is not None:
                client = Client.objects.get(id=id)
                if client:
                    serializer = ClientSerializer(client, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
            else:                
                client = Client.objects.filter(identification=identification).first()                
                if client is None:                
                    serializer = ClientSerializer(data=request.data)
                    if serializer.is_valid():                
                        serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    response_data={
                        "state":False,
                        "message":"El número de documento ya se encuentra registrado"
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