# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from login.forms import *
from bookmark.forms import signUpForm
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login
from .forms import UserLoginForm
from django.contrib.auth.models import User
from .models import Category,UserBookmark
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
            user = form.save()
            request.session['user'] = user.pk
            # user=User.objects.create_user(
            # email=form.cleaned_data['email'],
            # password = form.cleaned_data['Password'],
            # password2 = form.cleaned_data['Confirm password']
            # )
            # return HttpResponseRedirect('/register/success/')
            return render(request,'category.html')
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
        blist = get_bookmark(user)
        return render(request,'myprofile.html',{'blist': blist})
    return render(request,'login.html',{'form': form})

def register_success(request):
    return render(
        request,
        'success.html',
        )
    
def home_redirect(request):
    return redirect('/bookmark/')

def get_category(request):
    clist = request.POST.getlist("categories")
    user = request.session.get('user')
    print clist
    print user
    obj=Category(user_id=user,category=clist)
    obj.save()
    return HttpResponse("Registeration succesfull")
    # user.category=cname
    # user.save()
def save_bookmark(request):
    bmark = request.POST.get("url")
    user = request.user.pk
    obj = UserBookmark(user_id=user,bookmark=bmark)
    obj.save()
    blist = get_bookmark(user)
    return render(request,'myprofile.html',{'blist': blist})

def get_bookmark(user):
    blist = UserBookmark.objects.filter(user = user)
    return blist

def home(request):
    category=Category.objects.filter(user=request.user.pk)
    # bookmarks= UserBookmark.objects.values('bookmark').filter(tag__in = category).exclude(user=request.user.pk)
    # bookmarks = UserBookmark.objects.values('bookmark').filter(tag__in = ['java','android','python'])
    bookmarks = UserBookmark.objects.filter(tag__in = ['Java','Android','Python','Data Science','Data Analytics'])
    print bookmarks
    return render(request,'home.html')

def save_tag(request):
    tagslist = request.POST.getlist("tag")
    bookmark = request.POST.get("bookmark")
    print bookmark
    obj=UserBookmark.objects.get(bookmark = bookmark)
    user = request.user.pk
    obj.tag = tagslist
    obj.save()
    blist = get_bookmark(user)
    return render(request,'myprofile.html',{'blist' : blist})


        

    


