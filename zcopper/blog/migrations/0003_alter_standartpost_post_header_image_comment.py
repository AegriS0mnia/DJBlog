# Generated by Django 4.2.3 on 2023-08-10 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_standartpost_tags_alter_standartpost_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standartpost',
            name='post_header_image',
            field=models.ImageField(null=True, upload_to='photos/%d/%m/%Y', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, verbose_name='Текст комментария')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.standartpost')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['time_create'],
            },
        ),
    ]