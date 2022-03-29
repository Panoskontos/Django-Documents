from django.shortcuts import render
from django.http.response import JsonResponse
# Better than response
from rest_framework.response import Response
# Create your views here.
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        # here you create the overview of your api

        'Display product list': 'products/',

        '         ': '           ',
    }

    return Response(api_urls)


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
