from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.


def add_post(request):
    if request.method == 'POST':
        post = forms.PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('add_post')
    else:
        post = forms.PostForm()
    return render(request, 'posts/post.html', {'post': post})
