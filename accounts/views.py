from django.shortcuts import render,redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print('has been saved')
            return redirect('login')
        
    # request.method == GET 
    else:
        form = SignUpForm()

    return render(request,'registration/signup.html',{'form':form})
