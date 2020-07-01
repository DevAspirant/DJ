from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Product

# Create your views here.
def say_hi(request,name):
    return render(request, 'say-hi.html',{'name': name})

# workshop 1
def show_time(request):
    now = timezone.now()
    return HttpResponse(now)

# workshop 2
def product_list(request):
    products = Product.objects.all()
    description = Product.desc
    return render(request, 'products.html', { 'products' : products }, { 'des' : description})

