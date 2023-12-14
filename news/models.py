from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=25, verbose_name='Главный заголовок')
    title_text = models.CharField(max_length=50, verbose_name='Заголовок статьи')
    text = models.TextField(max_length=800, verbose_name='Текст статьи')
    image = models.ImageField(verbose_name='Главная фотография', upload_to='news/%Y/%m/%d')
    image_text = models.ImageField(verbose_name='Фото текста', upload_to='news/%Y/%m/%d', blank=True)
    comment = models.TextField(max_length=350, verbose_name='Дополнительный текст', blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')


    def __str__(self):
        return f'{self.title}, {self.pub_date}, {self.author}'