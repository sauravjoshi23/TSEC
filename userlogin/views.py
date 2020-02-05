from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import FormOne


def FormOneView(request):
    formone = FormOne()
    if request.method == 'POST':
        formone = FormOne(request.POST)
        
        if formone.is_valid():
            email = formone.cleaned_data.get('email')
            name = formone.cleaned_data.get('name')
            phone_number = formone.cleaned_data.get('phone_number')
            clubs = formone.cleaned_data.get('clubs')
            city = formone.cleaned_data.get('city')
            print("clubs = ", clubs)
            print("city = ", city)
            print(type(city))
            if clubs == 'Other' or city == 'Other':
                return render(request, 'userlogin/rejected.html')
                # redirect('/rejected')
            else :
                return render(request, 'userlogin/accepted.html')
                # redirect('/accepted')
    else:
        formone = FormOne()
    
    context = {
        'form' : formone
    }
    return render(request, 'userlogin/formone.html', context)

def RejectedView(request):
    return render(request, 'userlogin/accepted.html')

def AcceptedView(request):
    return render(requets, 'userlogin/rejected.html')


def index(request):
    return render(request, 'userlogin/index.html')

def RegisterView(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index_page')
    return render(request, 'userlogin/register.html', {'form': form})
