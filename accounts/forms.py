from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=13, required=False,help_text='Optional')
    last_name = forms.CharField( max_length=13, required=False,help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required information')

    class Meta:
       Model = User
       fields = ('username','password1','password2','first_name','last_name','email')
