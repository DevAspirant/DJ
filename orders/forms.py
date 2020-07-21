from django import forms
from .models import Orders

class OrderForm(forms.ModelForm):
    class  Meta:
        model = Orders
        fields = ('address',)

    def save(self,user):
        self.instance.user = user
        self.instance.save()

        for item in user.cart.items.all():
            self.instance.items.add(item)

        user.cart.items.clear()

        return self.instance         