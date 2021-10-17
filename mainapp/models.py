from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )

    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='цена',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество',
        default=0,
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class City(models.Model):
    name = models.CharField(
        verbose_name='Город',
        max_length=20,
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )

    phone = models.CharField(
        verbose_name='номер телефона',
        max_length=15,
    )

    email = models.CharField(
        verbose_name='Email',
        max_length=60,
    )

    address = models.CharField(
        verbose_name='адрес',
        max_length=100,
    )

    def __str__(self):
        return f"{self.address} ({self.city.name})"
