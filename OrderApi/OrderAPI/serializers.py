from django.db.models import fields
from rest_framework import serializers
from .models import Order, Adress, Product
from drf_writable_nested import WritableNestedModelSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__' 
        depth = 1

class OrderSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    product = ProductSerializer()
    adress = AdressSerializer()
    class Meta:
        model = Order
        fields = '__all__' 
