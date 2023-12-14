# Generated by Django 4.2.7 on 2023-12-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_alcohol_category_coffee_category_cola_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='alcohol',
        ),
        migrations.RemoveField(
            model_name='category',
            name='coffee',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cola',
        ),
        migrations.RemoveField(
            model_name='category',
            name='energy',
        ),
        migrations.RemoveField(
            model_name='category',
            name='fanta',
        ),
        migrations.RemoveField(
            model_name='category',
            name='juice',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='category',
            name='tonic',
        ),
        migrations.RemoveField(
            model_name='category',
            name='water',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
    ]