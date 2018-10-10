# from .models import Client
# from .serializers import ClientSerializer
# from rest_framework import routers, serializers, viewsets

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# def saveClient(request):
#     """
#     List all code vehicle, or create a new vehicle.
#     """
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ClientSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Client
from state.models import State
from .serializers import ClientSerializer

class ClientTask(APIView):   
    
    def get(self, request, format=None):
        print('cliente')
        id_ = request.GET.get('id')
        identification_ = request.GET.get('identification')
        try:
            if id_:
                client = Client.objects.get(id=id_)
            elif identification_:
                client = Client.objects.get(identification=identification_)
            else:
                clients = Client.objects.all()
                serializer = ClientSerializer(clients, many=True)
                return Response(serializer.data)

            if client:
                serializer = ClientSerializer(client)
                return Response(serializer.data)
            return Response(status=status.HTTP_404_NOT_FOUND)        
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)        
        

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
        serializer = ClientSerializer(data=request.data)
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