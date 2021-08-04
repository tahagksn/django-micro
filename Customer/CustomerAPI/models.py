from django.db import models
import uuid

from django.db.models.fields.related import OneToOneField


class Adress(models.Model):
    adressLine = models.TextField()
    city = models.TextField()
    country = models.TextField()
    city_code = models.IntegerField()

    
    class Meta:
        db_table = 'store_Adress'


class Customer (models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField( max_length=255)
    email = models.EmailField(unique=True)  
    createdAt = models.DateTimeField (auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'store_Customers'
        


    

    
