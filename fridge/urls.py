from django.urls import path
from fridge.views import fridge_view, fridge_add, fridge_delete, get_recipe, barcode_scan

app_name = "fridge"
urlpatterns = [
    path("", fridge_view, name="fridge"),
    path("add/", fridge_add, name="fridge_add"),
    path("<int:fridge_id>/delete/", fridge_delete, name="fridge_delete"),
    path("recipe/", get_recipe, name="get_recipe"),
    path("barcode/", barcode_scan, name="barcode"),
]