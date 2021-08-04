from rest_framework import serializers
from .models import Customer, Adress
from drf_writable_nested import WritableNestedModelSerializer

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = '__all__'


class CustomerSerializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    adress = AdressSerializer()
    class Meta:
        model = Customer
        fields = '__all__'

