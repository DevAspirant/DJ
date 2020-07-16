from django.urls import path 
from .views import add_to_cart,cart

urlpatterns = [
    path('',cart,name='cart'),
    path('add/<product_id>',add_to_cart,name='add_to_cart'),
]