from django.conf import settings
from django.db import models


class Product(models.Model):
    examination = models.ForeignKey(
        "examinations.MagneticResonanceImagingThreeTesla",
        on_delete=models.CASCADE,
        related_name="products",
    )
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.examination.name} - Quantity: {self.quantity}"


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="basket",
    )
    products = models.ManyToManyField(Product, related_name="baskets")
    add_datetime = models.DateTimeField(
        verbose_name="Ավելացման ամսաթիվ", auto_now_add=True
    )
