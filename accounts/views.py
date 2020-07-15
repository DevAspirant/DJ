from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import get_user_model
from django.http.response import HttpResponseBadRequest


from .forms import SignUpForm
from .utils import send_confirmation_email
from .tokens import confirm_email_token_generator


User = get_user_model()

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            send_confirmation_email(request, user)
            return render(request,'registeration/signup-success.html')
        
    # request.method == GET 
    else:
        form = SignUpForm()

    return render(request,'registration/signup.html',{'form':form})

def activate_email(request,uid,token):
    user = get_object_or_404(User,pk=uid)
    if confirm_email_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponseBadRequest('bad token')
