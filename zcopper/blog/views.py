from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from .models import StandartPost, Comment, Category
from .forms import AddPostForm, AddComment, RegisterUserForm, LoginUserForm
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


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
        return StandartPost.objects.filter(is_published=True).select_related('cat')


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


class ShowPost(View):
    model = StandartPost

    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(StandartPost, slug=post_slug)
        cats = Category.objects.annotate(Count('standartpost'))
        comment_form = AddComment()
        return render(request, 'blog/post.html',
                      context={'post': post, 'comment_form': comment_form, 'cats': cats})

    def post(self, request, post_slug, *args, **kwargs):
        comment_form = AddComment(request.POST)
        cats = Category.objects.annotate(Count('standartpost'))
        if comment_form.is_valid():
            text = request.POST['comment_text']
            username = self.request.user
            post = get_object_or_404(StandartPost, slug=post_slug)
            comment = Comment.objects.create(post=post, username=username, comment_text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'blog/post.html',
                      context={'comment_form': comment_form, 'cats': cats})


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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context.update(c_def)
        return context


def logout_user(request):
    logout(request)
    return redirect('login')


class AboutPage(DataMixin, ListView):
    model = StandartPost
    template_name = 'blog/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О сайте')
        context.update(c_def)
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1 align="center">Блинб, похоже такой странички нет🥲</h1>')
