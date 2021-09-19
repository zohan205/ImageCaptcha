from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .decorators import unuthenticated_user,allowed_users

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .forms import ImageForm

from .models import Image

import random

@login_required
def index(request):
    return render(request,'basicapp/index.html')

@unuthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Account has been created for '+username)
            return redirect('login')
    context = {'form':form}
    return render(request,'basicapp/registration.html',context)


@unuthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'basicapp/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required
@allowed_users(allowed_roles=['admin'])
def edit(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render (request,'basicapp/edit.html',{'form':form,'img':img})

@login_required
@allowed_users(allowed_roles=['customer'])
def challenge(request):
    data = Image.objects.order_by('?')[:1]
    return render(request,'basicapp/theChallenge.html',{'data':data})
