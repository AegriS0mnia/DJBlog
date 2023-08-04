from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import *

menu_buttons = [{'title': 'О сайте😵‍💫', 'url_name': 'about'},
                {'title': 'Главная🤐', 'url_name': 'home'},
                {'title': 'Добавить статью😳', 'url_name': 'add_page'},
                {'title': 'Регистрация😐/Войти🥵', 'url_name': 'login'},
                ]

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>', {'menu': menu_buttons})

def index(request):
    posts = StandartPost.objects.all()

    main_page_context = {'posts': posts, 'menu': menu_buttons, 'title': 'Главная страница',
                         'cat_selected': 0}

    return render(request, 'blog/index.html', context=main_page_context)


def show_category(request, cat_slug):
    posts = StandartPost.objects.filter(cat__slug=cat_slug)
    if len(posts) == 0:
        raise Http404

    category_context = {'posts': posts,
                        'menu': menu_buttons,
                        'title': 'Отображение по категориям',
                         'cat_selected': cat_slug}

    return render(request, 'blog/index.html', category_context)


def show_post(request, post_slug):
    post = get_object_or_404(StandartPost, slug=post_slug)
    post_context = {
        'post': post,
        'menu': menu_buttons,
        'title': post.title,
        'catselected': post.cat_id,
    }
    return render(request, 'blog/post.html', context=post_context)


def about(request):
    return render(request, 'blog/about.html', {'menu': menu_buttons})


def add_page(request):
    form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu': menu_buttons, 'title': 'Добавление статьи'})


def login(request):
    return render(request, 'blog/login.html', {'menu': menu_buttons})



