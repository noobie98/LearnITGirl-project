# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from login.forms import *
from bookmark.forms import signUpForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from .forms import UserLoginForm
# Create your views here.

def index(request):
        return render(
        request,
        'index.html',
    )
def register(request):
    if request.method == 'POST':
        form = signUpForm(request.POST) # Create a form instance and populate it with data from the request (binding):
        if form.is_valid():
            form.save()
            # user=User.objects.create_user(
            # email=form.cleaned_data['email'],
            # password = form.cleaned_data['Password'],
            # password2 = form.cleaned_data['Confirm password']
            # )
            # return HttpResponseRedirect('/register/success/')
            return render(request,'registerInterest.html')
# If this is a GET (or any other method) create the default form.
    else:
        form = signUpForm()
    return render(request, 'register.html', {'form': form})
def login_view(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username,password = password)
        # args = user
        args = {'user': request.user}
        login(request,user)
        return render(request,'profile.html',args)
    return render(request,'login.html',{'form': form})

def register_success(request):
    return render(
        request,
        'success.html',
        )
def home_redirect(request):
    return redirect('/bookmark/')
# def get_category(request):
#     cname = request.POST.get("dropdown1")
#     user.category=cname
#     user.save()


