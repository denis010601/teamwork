from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.FileField('Изображение', upload_to='brands_img')

    def __str__(self):
        return f'{self.title},{self.image}'
