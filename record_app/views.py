from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
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
    context={}
    return render(request, "login.html", context)

# testing git 
