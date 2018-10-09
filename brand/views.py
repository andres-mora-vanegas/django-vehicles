from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from brand.models import Brand
from brand.serializers import BrandSerializer
# Create your views here.

# class BrandViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Brand.objects.all().order_by('-date_joined')
#     serializer_class = BrandSerializer

@csrf_exempt
def brand_list(request):
    """
    List all code brand, or create a new brand.
    """
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = BrandSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def brand_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        brand = Brand.objects.get(pk=pk)
    except Brand.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return JsonResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(snippet, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     snippet.delete()
    #     return HttpResponse(status=204)