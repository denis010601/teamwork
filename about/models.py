from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="Соц сеть", blank=True, null=True)
    image = models.ImageField(upload_to='image/', verbose_name="иконка")
    social = models.URLField(max_length=150, verbose_name="ссылка", blank=True)

    def __str__(self):
        return f"{self.title}  |  {self.social}"
