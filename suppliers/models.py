from django.db import models


class Supplier(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]
    name = models.CharField(max_length=255, verbose_name='Название')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень в иерархии')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')

    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')
    country = models.CharField(max_length=255, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=25, verbose_name='Номер строения')

    debt = models.DecimalField(default=0, max_digits=30, decimal_places=2, verbose_name='Задолженность')
    creating_data = models.DateField(auto_now_add=True, verbose_name='Создание объекта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
