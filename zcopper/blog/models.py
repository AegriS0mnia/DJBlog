from django.db import models


class StandartPost(models.Model):
    title = models.CharField(max_length=255)
    post_author = models.TextField(blank=True)
    post_header_image = models.ImageField(upload_to='photos/%d/%m/%Y')
    post_text = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
