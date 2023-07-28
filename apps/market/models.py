from django.db import models
from apps.organizations.models import Concern, Organization


class Category(models.Model):
    name = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField('Наименование товара', max_length=150)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name='products'
    )

