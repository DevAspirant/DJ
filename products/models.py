from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    
    title = models.CharField(max_length=100)
     
    desc = models.CharField(max_length=500,blank=True, null=True) # to show the product description
    
    # for link the product
    def get_absolute_url(self):
        return reverse('product_details',args=(self.id,))

    # to show the product as string 
    def __str__(self):
        return self.title