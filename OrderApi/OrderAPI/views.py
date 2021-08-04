from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Order, Adress, Product
from .serializers import OrderSerializer, ProductSerializer
from rest_framework.response import Response
import requests

class OrderViewSet  (viewsets.ViewSet):

    def get_orders (self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response (serializer.data)

    def create (self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        customer_id = serializer.validated_data['customer_id']
        r = requests.get('http://customer_web:8001/api/v1/customer/api/<uuid4:customer_id>')
        if (r=='<Response[400]>'):
            return Response (status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data['order_id'], status=status.HTTP_201_CREATED)
    
    def update (self, request, pk=None):
        order = Order.objects.get(order_id=pk)
        serializer = OrderSerializer(instance=order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({True}, status=status.HTTP_201_CREATED)
    
    def delete (self, request, pk=None):
        order = Order.objects.get(order_id = pk)
        order.delete()
        return Response({True},status=status.HTTP_204_NO_CONTENT)
        
    
    def get_id (self, request, pk=None):
        
        order = Order.objects.get(order_id = pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def changeStatus (self, request, pk=None):
        order = Order.objects.get(order_id=pk)
        serializer = OrderSerializer(instance=order, data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({True}, status=status.HTTP_201_CREATED)


     