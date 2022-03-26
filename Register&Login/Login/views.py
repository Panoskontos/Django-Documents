from django.contrib.auth import authenticate, login
from .forms import *
from django.shortcuts import render, redirect


def loginview(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                return redirect('home')
            else:
                return redirect('login')
        else:
            form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'library/login.html', context)
