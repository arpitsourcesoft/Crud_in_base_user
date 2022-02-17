from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from .models import User
from django.http import HttpResponse
from .forms import login_account, userregistration

def home(request):
    data = User.objects.all() 
    print(data)  
    return render(request,template_name='home.html',context={'objects':data})

def index(request):    
    return render(request,template_name='index.html')


def showformdata(request):
    if request.method == 'GET':
        print("hello mai GET hu")
        form = userregistration(request.GET)
        return render(request, template_name = "signup.html", context={'form':form})

    if request.method == "POST":
        print("hello mai POST hu")
        form = userregistration(request.POST)
        print("hello mai userregistration hu")
        if form.is_valid():
            username = request.POST['username']
            # first_name = request.POST['first_name']
            # last_name = request.POST['last_name']
            email = request.POST['email']
            en = User.objects.create(username=username, email= email)
            en.save()
            print("hello mai form valid k baadka matter hu")
            return render(request, template_name = "signup.html", context={"form":form})

def login(request):
    if request.method == 'GET':
        
        form = login_account(request.GET)
        return render(request, template_name = "login.html", context={'form':form})

    if request.method == "POST":
        
        form = login_account(request.POST)
       
        if form.is_valid():
            password = request.POST['password']
            email = request.POST['email']
           
            print(request.user)
            return HttpResponseRedirect("/home/")
        
        
        return render(request, template_name = "login.html", context={"form":form})



