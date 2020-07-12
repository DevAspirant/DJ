from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Product
from products.forms import AddProductForm

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
    return render(request, 'products/products.html', { 'products' : products }, { 'des' : description})

# workhop 3 
def product_details(request,pk):
    product = get_object_or_404(Product,pk=pk)
    return render(request, 'products/product-details.html',{'product' : product})
  
#workshop 5 
def product_add(request):
    if request.method=="POST":
#        brand = request.POST["brand"]
#       title = request.POST["title"]
#        description = request.POST["desc"]
#        price = request.POST["price"]

#         add the product into DB
#        product = Product(brand=brand,title=title,desc=description,price=price)
#        product.save()
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save() 
            return render(request,'products/add-product-succes.html')
    else:
        form = AddProductForm()
    # solved 
    return render(request, 'products/product-add.html', {'form' : form}) 

def product_edit(request,pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method=="POST":
   
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save() 
            return render(request,'products/edit-product.html')
    else:
        form = AddProductForm(instance=product)
        return render(request, 'products/product-add.html', {'form' : form}) 

def product_delete(request,pk):
    product = get_object_or_404(Product,pk=pk)
    product.delete()
    return render(request,'products/delete-product.html')
  