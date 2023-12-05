from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=15, verbose_name='Текст')
    image = models.ImageField(verbose_name='Фото', upload_to='article/%Y/%m/%d', blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('news', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'