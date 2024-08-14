from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "User Created Successfully")
            form.save()
        else:
            print(form.errors)
    else:
        form = forms.RegisterForm()
    return render(request, 'signup/signup.html', {'forms': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            # is user is available in database
            user = authenticate(username=name, password=user_pass)
            if user is not None:
                login(request, user)
                print(user)
                return redirect('/user-signup/user_profile/')
    else:
        form = AuthenticationForm()
    return render(request, 'signup/login.html', {'forms': form})


def profile(request):
    return render(request, 'signup/userprofile.html', {'users': request.user})
