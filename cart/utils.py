from .models import Cart


def get_current_cart(request):
    try:
        cart_id = request.session.get("cart")
        cart = Cart.objects.prefetch_related().get(pk=cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create()

    request.session["cart"] = cart.pk
    return cart
