from django.contrib import admin
from django.db import models


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

    def __str__(self):
        return f"{self.title}, {self.volume}"

