from django.db.models import Count

from .models import *

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('standartpost'))

        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
