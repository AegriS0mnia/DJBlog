from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu_buttons = [{'title': 'О сайте😵‍💫', 'url_name': 'about'},
                {'title': 'Главная🤐', 'url_name': 'home'},
                {'title': 'Добавить статью😳', 'url_name': 'add_page'},
                {'title': 'Регистрация😐/Войти🥵', 'url_name': 'login'},
                ]

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>', {'menu': menu_buttons})

def index(request):
    posts = StandartPost.objects.all()
    cats = Category.objects.all()

    main_page_context = {'posts': posts, 'cats': cats, 'menu': menu_buttons, 'title': 'Главная страница',
                         'cat_selected': 0}

    return render(request, 'blog/index.html', context=main_page_context)


def show_category(request, cat_id):
    posts = StandartPost.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    if len(posts) == 0:
        raise Http404

    category_context = {'posts': posts,
                        'cats': cats,
                        'menu': menu_buttons,
                        'title': 'Отображение по категориям',
                         'cat_selected': cat_id}
    return render(request, 'blog/index.html', category_context)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с номером: {post_id}")


def about(request):
    return render(request, 'blog/about.html', {'menu': menu_buttons})


def add_page(request):
    return render(request, 'blog/addpage.html', {'menu': menu_buttons})


def login(request):
    return render(request, 'blog/login.html', {'menu': menu_buttons})



