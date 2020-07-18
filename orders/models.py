from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

# Create your models here.
class Orders(models.Model):
    user = models.OneToOneField(User, related_name='order',on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True) 
    #address = models.OneToOneField(User,related_name='order')

    def __str__(self):
        return str(self.user)
        
# do not understand yet 
'''@receiver(post_save, sender=User)
def create_order_cart(sender, instance, created, **kwargs):
    if created:
        Orders.objects.create(user=instance)'''
    
       
    
