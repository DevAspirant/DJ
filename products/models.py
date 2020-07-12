from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    
    brand = models.CharField(max_length=100)

    title = models.CharField(max_length=100)
     
    desc = models.CharField(max_length=500,blank=True, null=True) # to show the product description

    price = models.PositiveIntegerField(blank=True,null=True) # price 

    created_date = models.DateTimeField(auto_now_add=True,blank=True,null=True) # created date 
    
    image = models.ImageField(upload_to='product/',null=True)

    # for link the product
    def get_absolute_url(self):
        return reverse('product_details',args=(self.id,))

    # to show the product as string 
    def __str__(self):
        return self.title