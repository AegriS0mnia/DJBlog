from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu_buttons = [{'title': 'О сайте😵‍💫', 'url_name': 'about'},
                {'title': 'Главная🤐', 'url_name': 'home'},
                {'title': 'Добавить статью😳', 'url_name': 'add_page'},
                {'title': 'Войти🥵', 'url_name': 'login'},
                ]


def index(request):
    posts = StandartPost.objects.all()
    main_page_context = {'posts': posts, 'menu': menu_buttons, 'title': 'Главная страница'}
    return render(request, 'blog/index.html', context=main_page_context)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с номером: {post_id}")

def about(request):
    return render(request, 'blog/about.html', )


def add_page(request):
    return render(request, 'blog/addpage.html', )


def login(request):
    return render(request, 'blog/login.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>')
