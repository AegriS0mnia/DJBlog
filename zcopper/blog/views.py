from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *

menu_buttons = [{'title': 'О сайте‍', 'url_name': 'about'},
                {'title': 'Главная', 'url_name': 'home'},
                {'title': 'Добавить статью', 'url_name': 'add_page'},
                {'title': 'Регистрация/Войти', 'url_name': 'login'},
                ]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>', {'menu': menu_buttons})


class BlogHome(ListView):
    model = StandartPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_buttons
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return StandartPost.objects.filter(is_published=True)


class BlogCategory(ListView):
    model = StandartPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_buttons
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return StandartPost.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DetailView):
    model = StandartPost
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_buttons
        context['title'] = 'Добавление статьи'
        return context


def about(request):
    return render(request, 'blog/about.html', {'menu': menu_buttons})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu_buttons
        context['title'] = 'Добавление статьи'
        return context


def login(request):
    return render(request, 'blog/login.html', {'menu': menu_buttons})
