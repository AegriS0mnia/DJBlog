from .models import *

menu_buttons = [{'title': 'О сайте', 'url_name': 'about'},
                {'title': 'Главная', 'url_name': 'home'},
                {'title': 'Добавить статью', 'url_name': 'add_page'},
                {'title': 'Регистрация/Войти', 'url_name': 'login'},
                ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu_buttons
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context