from django.contrib import admin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from personal_account.models import CastomUser


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название", blank=True, null=True)
    image = models.ImageField(upload_to='image/', verbose_name="Фото продукта")
    volume = models.CharField(max_length=100, verbose_name="Объем", blank=True, null=True)
    packaging = models.CharField(max_length=100, verbose_name="Количество в упаковке", blank=True, null=True)
    netto = models.CharField(max_length=100, verbose_name="Масса нетто", blank=True, null=True)
    brutto = models.CharField(max_length=100, verbose_name="Масса брутто", blank=True, null=True)
    delivery = models.CharField(max_length=100, verbose_name="Время доставки", blank=True, null=True)
    minimal_order = models.CharField(max_length=100, verbose_name="Минимальная партия", blank=True, null=True)
    barcode = models.PositiveIntegerField(verbose_name="Код продукта")
    pcs_truck = models.PositiveIntegerField(verbose_name="Штук в фуре")
    pallets_truck = models.PositiveIntegerField(verbose_name="Паллет в фуре")
    cases_truck = models.PositiveIntegerField(verbose_name="Упаковок в фуре")
    gross_weight = models.FloatField(verbose_name="Общая масса, кг")
    description = models.TextField(verbose_name="Описание", blank=True)

    @property
    def no_of_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        return len(ratings)

    @property
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rating in ratings:
            sum = sum + rating.value

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return f"{self.title}, {self.volume}"

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CastomUser, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

class Rating(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CastomUser, on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return str(self.product) + "---" + str(self.user)