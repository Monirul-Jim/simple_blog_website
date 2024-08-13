from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.contrib import messages
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


def login(request):
    return render(request, 'signup/login.html')
