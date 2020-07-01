from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
     
    desc = models.CharField(max_length=500,blank=True, null=True) # to show the product description
    
    # to show the product as string 
    def __str__(self):
        return self.title

    

