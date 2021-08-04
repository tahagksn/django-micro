from django.urls import path, include
from .views import CustomerViewSet



urlpatterns = [
    path('api', CustomerViewSet.as_view({
        'get':'get_customers',
        'post':'create'
    })),
    path('api/<str:pk>',CustomerViewSet.as_view({
        'put':'update',
        'delete':'delete',
        'get':'get_id'
        
    }))
]
