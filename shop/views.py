from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import *

class Purchases(viewsets.ModelViewSet):
    queryset = Saled.objects.all()
    serializer_class = SaledSerializer

    def list(self, request, *args, **kwargs):
        data = list(Saled.objects.all().values())
        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        data = list(Saled.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        product_serializer_data = SaledSerializer(data=request.data)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Added Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "please fill the datails", "status": status_code})

    def destroy(self, request, *args, **kwargs):
        product_data = Saled.objects.filter(id=kwargs['pk'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})

    def update(self, request, *args, **kwargs):
        product_details = Saled.objects.get(id=kwargs['pk'])
        product_serializer_data = SaledSerializer(
            product_details, data=request.data, partial=True)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
