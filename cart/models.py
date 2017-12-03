from django.db import models

from shop.models import Sku


class Cart(models.Model):
    pass


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items",
        related_query_name="item",
    )

    sku = models.ForeignKey(
        Sku,
        on_delete=models.CASCADE,
        related_name="+",
    )
