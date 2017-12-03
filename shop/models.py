from django.db import models


class ProductManager(models.Manager):
    def in_stock(self):
        products_in_stock = Sku.available_skus.values_list("product", flat=True)
        return self.filter(pk__in=products_in_stock)


class Product(models.Model):
    """Available products.
    """

    name = models.CharField(max_length=250)
    description = models.TextField()

    price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
    )

    products = ProductManager()

    def __str__(self):
        return self.name


class AvailableSkuManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Sku.STATUS_AVAILABLE)


class Sku(models.Model):
    """Individual stock-keeping units.
    """

    STATUS_AVAILABLE = "available"
    STATUS_RESERVED = "reserved"
    STATUS_SOLD = "sold"
    STATUSES = [
        (STATUS_AVAILABLE, "Available"),
        (STATUS_RESERVED, "Reserved"),
        (STATUS_SOLD, "Sold"),
    ]

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        choices=STATUSES,
        default=STATUS_AVAILABLE,
        max_length=max(len(v) for v, _ in STATUSES),
    )

    available_skus = AvailableSkuManager()

    def __str__(self):
        return f"{self.product.name}@{self.pk}"
