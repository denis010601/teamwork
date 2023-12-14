# Generated by Django 4.2.7 on 2023-12-14 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Главный заголовок')),
                ('title_text', models.CharField(max_length=50, verbose_name='Заголовок статьи')),
                ('text', models.TextField(max_length=800, verbose_name='Текст статьи')),
                ('image', models.ImageField(upload_to='news/%Y/%m/%d', verbose_name='Главная фотография')),
                ('image_text', models.ImageField(blank=True, upload_to='news/%Y/%m/%d', verbose_name='Фото текста')),
                ('comment', models.TextField(blank=True, max_length=350, verbose_name='Дополнительный текст')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
