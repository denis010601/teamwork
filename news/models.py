from django.db import models
from personal_account.models import CastomUser

class News(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок')
    text = models.TextField(max_length=250, verbose_name='Текст')
    image = models.ImageField(verbose_name='Фото', upload_to='news/%Y/%m/%d', blank=True)
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(CastomUser, on_delete=models.CASCADE, verbose_name='Автор')


    def __str__(self):
        return f'{self.title}'