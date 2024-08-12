from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def home(request):
    data = Post.objects.all()
    # for i in data:
    #     for j in i.category.all():
    #         print(j)
    # print(data)
    return render(request, 'home.html', {'data': data})
