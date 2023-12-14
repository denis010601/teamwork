# Generated by Django 4.2.7 on 2023-12-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото продукта')),
                ('volume', models.CharField(blank=True, max_length=100, null=True, verbose_name='Объем')),
                ('packaging', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество в упаковке')),
                ('netto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Масса нетто')),
                ('brutto', models.CharField(blank=True, max_length=100, null=True, verbose_name='Масса брутто')),
                ('delivery', models.CharField(blank=True, max_length=100, null=True, verbose_name='Время доставки')),
                ('minimal_order', models.CharField(blank=True, max_length=100, null=True, verbose_name='Минимальная партия')),
                ('barcode', models.PositiveIntegerField(verbose_name='Код продукта')),
                ('pcs_truck', models.PositiveIntegerField(verbose_name='Штук в фуре')),
                ('pallets_truck', models.PositiveIntegerField(verbose_name='Паллет в фуре')),
                ('cases_truck', models.PositiveIntegerField(verbose_name='Упаковок в фуре')),
                ('gross_weight', models.FloatField(verbose_name='Общая масса, кг')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
    ]
