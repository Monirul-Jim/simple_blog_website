from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
# Create your views here.


def add_author(request):
    if request.method == "POST":
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add-author')
    else:
        author_form = forms.AuthorForm()
    return render(request, 'author/author.html', {'forms': author_form})
