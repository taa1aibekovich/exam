# Generated by Django 5.1.6 on 2025-02-08 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стартовая цена')),
                ('min_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Минимальная цена')),
                ('status', models.CharField(choices=[('Активен', 'Активен'), ('Завершен', 'Завершен'), ('Отменен', 'Отменен')], default='Активен', max_length=20, verbose_name='Статус')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('администратор', 'администратор'), ('продавец', 'продавец'), ('покупатель', 'покупатель')], default='покупатель', max_length=32),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Размер ставки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='app.auction')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=65, verbose_name='Марка')),
                ('model', models.CharField(max_length=65, verbose_name='Модель')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('fuel_type', models.CharField(max_length=32, verbose_name='Тип топлива')),
                ('transmission', models.CharField(max_length=32, verbose_name='Коробка передач')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField()),
                ('images', models.ImageField(blank=True, null=True, upload_to='')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='auction',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.car', verbose_name='auction'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_buyer', to=settings.AUTH_USER_MODEL, verbose_name='given_feedback')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_seler', to=settings.AUTH_USER_MODEL, verbose_name='received_feedback')),
            ],
        ),
    ]
