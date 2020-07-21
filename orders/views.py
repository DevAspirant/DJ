from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Orders
from products.models import Product
from .forms import OrderForm

# Create your views here.
#@login_required
def make_order(request):
    user = request.user
    form = OrderForm(request.POST,request.FILES)
    order = form.save(user)
    return render(request,'orders/order.html',{'form' : form })
    

    

def order(request):
    order = Orders.objects.all()
    return render(request, 'orders/order_list.html',{'order':order})