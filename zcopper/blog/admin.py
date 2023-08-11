from django.contrib import admin
from blog.models import StandartPost, Category, Comment


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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'time_create')
    list_display_links = ('comment_text',)
    search_fields = ('username', )


admin.site.register(StandartPost, StandartPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
