from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import UserLoginForm


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("valid")
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            context = {
                'form': form,
                'error': "Invalid username or password !!"
            }
            return render(request, 'accounts/login.html', context)

    form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')