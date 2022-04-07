from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
# Create your views here.
from django.contrib import auth


def home(request):
    return render(request, 'myapp/home.html', {})


def register(request):
    form = PublisherForm()
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = CustomUser.objects.get(username=username)
            user.user_type = 'student'
            user.save()

            publisher = Publisher(username=user)
            publisher.save()

            return redirect('home')
    context = {'form': form}
    return render(request, 'myapp/register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            custom_user = CustomUser.objects.get(
                username=username, password=password)
            print(custom_user)
            user = custom_user
            if user is None:
                return redirect('login')
            else:
                print(user.user_type)
                auth.login(request, user)
                return redirect('home')
    context = {'form': form}
    return render(request, 'myapp/register.html', context)
