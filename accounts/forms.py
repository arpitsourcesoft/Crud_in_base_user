from django import forms
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from urllib import request

class userregistration(forms.Form):
    
    username =  forms.CharField()
    email = forms.EmailField()
    mobile = forms.IntegerField()
    password =forms.CharField(widget=forms.PasswordInput)
   


class login_account (forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)
