from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def add_post(request):
    return render(request, 'posts/post.html')