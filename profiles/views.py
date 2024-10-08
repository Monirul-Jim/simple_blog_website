from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.


def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = forms.ProfileForm
    return render(request, 'profiles/profile.html', {'profile': profile_form})
