from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from products.models import Product

User = get_user_model()

# Create your models here.
# = Order
class Orders(models.Model):
    user = models.ForeignKey(User, related_name='make_order',on_delete=models.CASCADE) # related_name='orders'
    items = models.ManyToManyField(Product)
    updated_at = models.DateTimeField(auto_now=True) # = created_at
    address = models.CharField(max_length=256)

    def __str__(self):
        return f'Order {self.id} bt {self.user}'
        

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price
        return total    

# do not understand yet 
'''@receiver(post_save, sender=User)
def create_order_cart(sender, instance, created, **kwargs):
    if created:
        Orders.objects.create(user=instance)'''
    
       
    
