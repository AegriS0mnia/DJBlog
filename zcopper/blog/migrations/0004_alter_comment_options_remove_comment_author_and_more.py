# Generated by Django 4.2.3 on 2023-08-11 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_standartpost_post_header_image_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-time_create'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
