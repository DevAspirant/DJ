from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required


from products.models import Product
from .models import Cart

# Create your views here.
@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    cart = Cart.objects.get(user=request.user)
    cart.items.add(product)

    return redirect('')

@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()

    return render(request,'carts/cart.html',{'products': products })