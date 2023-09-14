from django.urls import path
from fridge.views import fridge_view, fridge_add, fridge_delete

app_name = "fridge"
urlpatterns = [
    path("", fridge_view, name="fridge"),
    path("add/", fridge_add, name="fridge_add"),
    path("<int:fridge_id>/delete/", fridge_delete, name="fridge_delete"),
]