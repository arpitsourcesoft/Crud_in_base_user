from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.urls import is_valid_path
from .models import User
from django.http import HttpResponse
from .forms import login_account, userregistration
from django.contrib.auth import authenticate, login

def home(request):
    data = User.objects.all() 
    return render(request,template_name='home.html',context={'objects':data})

def index(request):    
    return render(request,template_name='index.html')


def showformdata(request):
    if request.method == 'GET':
        
        form = userregistration(request.GET)
        print(type(form))
        return render(request, template_name = "signup.html", context={'form':form})

    if request.method == "POST":
        form = userregistration(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            mobile = request.POST['mobile']
            en = User.objects.create(username=username, email= email, mobile= mobile)
            en.set_password(password)
            en.save()
            return render(request, template_name = "signup.html", context={"form":form})

def user_login(request):
    if request.method == 'GET':        
        form = login_account(request.GET)
        return render(request, template_name = "login.html", context={'form':form})

    if request.method == "POST":        
        form = login_account(request.POST)
       
        if form.is_valid():
            password = request.POST['password']
            email = request.POST['email']           
            # print(request.user)
            test_user = User.objects.get(email=email)
            print("check password------->", test_user.check_password(password))
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/home/")
            else:
                return HttpResponse("Invalid Creadentials")

        return render(request, template_name = "login.html", context={"form":form})

