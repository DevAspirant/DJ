from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Product


# Create your views here.
def home_page(request):
    return render(request,'index.html')

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
    price = Product.price
    return render(request, 'products/products.html', { 'products' : products }, { 'des' : description})

# workhop 3 
def product_details(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request, 'products/product-details.html',{'product' : product})
  

