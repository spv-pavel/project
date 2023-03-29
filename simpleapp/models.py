from django.core.validators import MinValueValidator
from django.db import models


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,  # названия товаров не должны повторяться
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0, 'Quantity should be >= 0')],
    )
    # поле категории будет ссылаться на модель категории
    # все продукты в категории будут доступны через поле products
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name}: {self.quantity}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
