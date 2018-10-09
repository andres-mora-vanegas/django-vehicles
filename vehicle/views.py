from django.shortcuts import render
from .models import Vehicle
from .serializers import VehicleSerializer

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def vehicle_list(request):
    """
    List all code vehicle, or create a new vehicle.
    """    
    if request.method == 'GET':
        brand_=request.GET.get('brand')        
        if brand_ is not None:
            vehicles = Vehicle.objects.filter(brand=brand_)    
        else:
            vehicles = Vehicle.objects.all()    

        serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def vehicle_detail(request, pk):
    """
    Retrieve, update or delete a code vehicle.
    """
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return JsonResponse(serializer.data)