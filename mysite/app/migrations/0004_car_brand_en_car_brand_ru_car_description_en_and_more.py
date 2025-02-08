# Generated by Django 5.1.6 on 2025-02-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_car_fuel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand_en',
            field=models.CharField(max_length=65, null=True, verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='car',
            name='brand_ru',
            field=models.CharField(max_length=65, null=True, verbose_name='Марка'),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='model_en',
            field=models.CharField(max_length=65, null=True, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='car',
            name='model_ru',
            field=models.CharField(max_length=65, null=True, verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_en',
            field=models.CharField(max_length=32, null=True, verbose_name='Коробка передач'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_ru',
            field=models.CharField(max_length=32, null=True, verbose_name='Коробка передач'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='comment_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='comment_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
