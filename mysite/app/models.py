from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()
    role_choices = (
        ('администратор','администратор'),
        ('продавец', 'продавец'),
        ('покупатель', 'покупатель')
    )
    role = models.CharField(max_length=32, choices=role_choices, default='покупатель')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Car(models.Model):
    brand = models.CharField(max_length=65, verbose_name='Марка')
    model = models.CharField(max_length=65, verbose_name='Модель')
    year = models.IntegerField(verbose_name='Год выпуска')
    status_choices = (
        ('бензин', 'бензин'),
        ('газ', 'газ'),
        ('дизел', 'дизел'),
    )
    fuel_type = models.CharField(max_length=20, choices=status_choices, verbose_name="Тип топлива")

    transmission = models.CharField(max_length=32,verbose_name='Коробка передач')
    mileage = models.IntegerField(verbose_name='Пробег')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField()
    images = models.ImageField(null=True, blank=True)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return f'{self.brand} - {self.model}'


class Auction(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name='auction')
    start_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стартовая цена')
    min_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Минимальная цена')
    status_choices = (
        ('Активен', 'Активен'),
        ('Завершен', 'Завершен'),
        ('Отменен', 'Отменен'),
    )
    status = models.CharField(max_length=20, choices=status_choices, default='Активен', verbose_name="Статус")

    def __str__(self):
        return f'{self.car} - {self.start_price}'

class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Размер ставки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.auction} - {self.amount}'

class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='received_feedback', related_name='feedback_seler')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='given_feedback', related_name='feedback_buyer')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)],)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.seller} - {self.rating}'
