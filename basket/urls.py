from django.urls import path
import basket.views as basket
from .apps import BasketConfig

app_name = BasketConfig.name

urlpatterns = [
    path("", basket.basket, name="view"),
    path("add/<int:pk>/", basket.basket_add, name="add"),
    path("remove/<int:pk>/", basket.basket_remove, name="remove"),
]
