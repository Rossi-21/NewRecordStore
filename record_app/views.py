from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.models import Group

def home(request):
    return render(request, "index.html")

def registerUser(request):
    #bring in the CreateUserForm from forms.py
    form = CreateUserForm()

    if request.method == 'POST':
        #if the request is a POST request, fill in the form with the data from the user
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            user = form.save()

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            return redirect('home')
    
    context = {
        'form' : form
        }

    return render(request, 'register.html', context)

# Create your views here.
