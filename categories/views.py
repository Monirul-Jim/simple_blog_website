from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def add_category(request):
    return render(request, 'categories/category.html')
