from django.shortcuts import render

from .models import Product


def index(request):
    products = list(Product.products.in_stock().all())
    return render(request, "shop/index.html", {
        "products": products,
    })
