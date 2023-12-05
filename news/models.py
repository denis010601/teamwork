from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=15, verbose_name='Текст')

    def __str__(self):
        return f'{self.title}, {self.text}'