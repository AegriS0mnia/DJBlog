from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

def index(request):
    posts = StandartPost.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>')
