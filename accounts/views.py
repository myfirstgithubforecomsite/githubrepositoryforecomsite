from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method=="POST":
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']
        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.save();
            return redirect('/')
        else:
            print("password do not match")
            messages.info(request,'password do not match')
            return render(request, 'registration.html')

    else:
        return render(request,'registration.html')


def login(request, none=None):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        if user is not none:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


