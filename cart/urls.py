from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path("add/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:sku_id>", views.remove_from_cart, name="remove_from_cart"),
]
