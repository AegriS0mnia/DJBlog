from django.contrib import admin
from blog.models import StandartPost, Category


class StandartPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post_text', 'time_create', 'post_header_image', 'is_published')
    list_display_links = ('id', 'post_text')
    search_fields = ('title', 'post_text')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(StandartPost, StandartPostAdmin)
admin.site.register(Category, CategoryAdmin)
