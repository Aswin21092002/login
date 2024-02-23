from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

@login_required
def home(request):
    return render(request, 'home.html')