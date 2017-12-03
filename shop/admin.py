from django.contrib import admin

from .models import Product, Sku


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    pass
