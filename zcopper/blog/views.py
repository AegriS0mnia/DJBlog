from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .forms import *
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin

menu_buttons = [{'title': 'О сайте‍', 'url_name': 'about'},
                {'title': 'Главная', 'url_name': 'home'},
                {'title': 'Добавить статью', 'url_name': 'add_page'},
                ]


class BlogHome(DataMixin, ListView):
    model = StandartPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        context.update(c_def)
        return context

    def get_queryset(self):
        return StandartPost.objects.filter(is_published=True)


class BlogCategory(DataMixin, ListView):
    model = StandartPost
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        context.update(c_def)
        return context

    def get_queryset(self):
        return StandartPost.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class ShowPost(DataMixin, DetailView):
    model = StandartPost
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        context.update(c_def)
        return context


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        context.update(c_def)
        return context

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context.update(c_def)
        return context
def login(request):
    return render(request, 'blog/login.html', {'menu': menu_buttons})


def about(request):
    return render(request, 'blog/about.html', {'menu': menu_buttons})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странчки нет🥲</h1>', {'menu': menu_buttons})
