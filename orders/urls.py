from django.urls import path
from .views import make_order,order

urlpatterns = [
    path('orders/',order,name='order.html'),
    path('orders/new/',make_order,name='make_order'),
]