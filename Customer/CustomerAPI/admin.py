from .models import Adress, Customer
from django.contrib import admin
from .models import Customer, Adress
# Register your models here.
admin.site.register(Customer)
admin.site.register(Adress)
