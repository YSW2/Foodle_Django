from django.urls import path
from fridge.views import fridge_view

app_name = "fridge"
urlpatterns = [
    path("fridge/", fridge_view, name="fridge"),
]