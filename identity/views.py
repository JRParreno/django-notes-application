from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        error_message = "Username and password doesn't exists"

    return render(request, 'identity/custom-login.html', {"error_message": error_message})


def login_form_view(request):
    error_message = ''
    form = LoginForm()
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('home')
        error_message = "Username and password doesn't exists"

    return render(request, 'identity/custom-login-form.html', {"error_message": error_message, "form": form})
