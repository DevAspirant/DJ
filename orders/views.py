from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Orders
from products.models import Product

# Create your views here.
#@login_required
def make_order(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    order = Orders.objects.get(user=request.user)
    order.items.add(product)

    return redirect('product_list')

def order(request):
    user = request.user 
    product = user.order.items.all()

    return render(request, 'orders/order.html',{ 'product' : product })