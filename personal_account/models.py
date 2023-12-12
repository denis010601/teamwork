from django.db import models
from django.contrib.auth.models import AbstractUser


class CastomUser(AbstractUser):
    first_name = models.CharField(max_length=250, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=250, verbose_name="Фамилия", blank=True, null=True)
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    mail = models.CharField(max_length=50, null=True, blank=True)
