from django.db import models
import uuid

from django.db.models.base import Model


class Product (models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    imageURL = models.TextField()
    name = models.TextField ()


class Adress (models.Model):
    adressLine = models.TextField()
    city = models.TextField()
    country = models.TextField()
    city_code = models.IntegerField(default=34)
  

    
class Order (models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    customer_id = models.UUIDField(primary_key=False, editable=True, unique=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.TextField(default='NEW')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE,null=True)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE,null=True)
