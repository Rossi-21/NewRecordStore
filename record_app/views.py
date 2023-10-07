from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

def home(request):
    if request.user.is_authenticated:

        context = {}
        return render(request, "index.html", context)

    else:
        return redirect('login')

def registerUser(request):
    #bring in the CreateUserForm from forms.py
    form = CreateUserForm()

    if request.method == 'POST':
        #if the request is a POST request, fill in the form with the data from the user
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            #group = Group.objects.get(name='customer')
            #user.groups.add(group)
            login(request, user)


            return redirect('home')
    
    context = {
        'form' : form
        }

    return render(request, 'register.html', context)

def loginUser(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context={}

    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')
