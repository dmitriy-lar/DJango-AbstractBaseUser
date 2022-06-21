from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .admin import UserCreationForm
from .forms import UserLoginForm

def index(request):
    return render(request, 'auth_test/index.html')


def register_user(request):
    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # first_name = form.cleaned_data.get('first_name')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['form'] = form
    else:
        form = UserCreationForm()
        context['form'] = form
    return render(request, 'auth_test/reg.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def login_user(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    context['form'] = form
    return render(request, 'auth_test/login.html', context)