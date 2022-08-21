from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import *;
from .models import *;

def home(request):
    return render(request, 'pages/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'pages/register.html', context)

def management(request):
    if request.method == 'POST':
        form = ManagementForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('home')
    else:
        form = ManagementForm()

    context = {'form': form}
    return render(request, 'pages/management.html', context)


def work(request):
    work_list = Management.objects.all()
    context = {'work_list': work_list}
    return render(request, 'pages/managementlist.html', context)