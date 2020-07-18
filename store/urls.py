"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import redirect
from products.views import home_page
from products.views import say_hi
from products.views import show_time
from django.conf import settings
from django.conf.urls.static import static


def home(request):
    return redirect('product_list')

urlpatterns = [
    #path('',home_page),
    path('admin/', admin.site.urls),
    path('say_hi/<str:name>',say_hi),
    path('show_time/',show_time),
    path('accounts/',include('accounts.urls')),
    path('',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('order/',include('orders.urls')),
    path('',home,name='home'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
