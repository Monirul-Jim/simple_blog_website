from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . models import Post
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


def edit_post(request, id):
    post_forms = Post.objects.get(pk=id)
    post = forms.PostForm(instance=post_forms)
    if request.method == 'POST':
        post = forms.PostForm(request.POST, instance=post_forms)
        if post.is_valid():
            post.save()
            return redirect('home')

    return render(request, 'posts/post.html', {'post': post})


def delete_post(request, id):
    post_forms = Post.objects.get(pk=id)
    post_forms.delete()
    return redirect('home')
