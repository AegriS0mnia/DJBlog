from taggit.managers import TaggableManager
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class StandartPost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    post_author = models.TextField(blank=True, verbose_name='Автор')
    post_header_image = models.ImageField(upload_to='photos/%d/%m/%Y', null=True, verbose_name='Изображение')
    post_text = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(StandartPost, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    comment_text = models.TextField(blank=True, verbose_name='Текст комментария')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_create']

    def __str__(self):
        return self.comment_text
