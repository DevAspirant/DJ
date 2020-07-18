from django.urls import path
from .views import make_order,order

urlpatterns = [
    path('',order,name='order'),
    path('order/<product_id>',make_order,name='make_order'),
]