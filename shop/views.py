from cart.utils import get_current_cart
from django.shortcuts import render

from .models import Product


def index(request):
    cart = get_current_cart(request)
    cart_items = list(cart.items.all())
    cart_total = sum(item.sku.product.price for item in cart_items)
    products = list(Product.products.in_stock().all())
    return render(request, "shop/index.html", {
        "cart": cart,
        "cart_items": cart_items,
        "cart_total": cart_total,
        "products": products,
    })
