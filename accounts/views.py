from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid deatails")
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method=="POST":

        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_pass = request.POST['re_pass']

        if password == re_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save();
                print("user created")
        else:
            print("password not match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')