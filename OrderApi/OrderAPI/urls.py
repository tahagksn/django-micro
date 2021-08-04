from django.urls import path
from .views import OrderViewSet



urlpatterns = [
    path('api', OrderViewSet.as_view({
        'get':'get_orders',
        'post':'create'
    })),
    path('api/<str:pk>',OrderViewSet.as_view({
        'put':'update',
        'delete':'delete',
        'get':'get_id'
        
    })),
    path('api/<str:pk>/status',OrderViewSet.as_view({
        'put':'changeStatus',
        
    })),
    path('api/multiple/get', OrderViewSet.as_view({
        'post':'get_multiple_id'
        }))
]
 