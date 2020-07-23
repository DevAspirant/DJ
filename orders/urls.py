from django.urls import path
from .views import make_order,order

urlpatterns = [
    path('',order,name='order.html'),
    path('new',make_order,name='make_order'),
]