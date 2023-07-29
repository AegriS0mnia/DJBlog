from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return render(request, 'blog/base.html',
                  {'title': 'Привет, мой хороший(ая)❤️! Ты на главной странице нашего блога.'})


def about(request):
    return render(request, 'blog/about.html', {'title': 'О сайте'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>')
