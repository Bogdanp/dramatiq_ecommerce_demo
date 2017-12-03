from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product, SkuNotAvailable

from .utils import get_current_cart


@require_POST
def add_to_cart(request, product_id):
    try:
        with transaction.atomic():
            product = get_object_or_404(Product, pk=product_id)
            sku = product.get_next_available_sku()
            sku.reserve()
            cart = get_current_cart(request)
            cart.items.create(sku=sku)

        messages.add_message(
            request, messages.INFO,
            "The product has been added to your cart!",
        )
        return redirect("shop:index")
    except SkuNotAvailable:
        messages.add_message(
            request, messages.ERROR,
            "That product has gone out of stock.",
        )
        return redirect("shop:index")


@require_POST
def remove_from_cart(request, sku_id):
    with transaction.atomic():
        cart = get_current_cart(request)
        item = cart.items.filter(sku=sku_id).first()
        item.sku.unreserve()
        item.delete()

    messages.add_message(
        request, messages.INFO,
        "The product has been removed from your cart.",
    )
    return redirect("shop:index")
