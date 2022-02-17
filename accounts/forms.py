from django import forms
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from urllib import request

class userregistration(forms.Form):
    
    username =  forms.CharField()
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    password =forms.CharField(widget=forms.PasswordInput)
   


class login_account (forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget= forms.PasswordInput)
