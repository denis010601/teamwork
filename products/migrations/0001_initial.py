# Generated by Django 4.2.7 on 2023-12-26 11:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
