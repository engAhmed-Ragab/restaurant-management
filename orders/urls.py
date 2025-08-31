# orders/urls.py
from django.urls import path
from .views import OrderList, order_create, order_update, OrderDelete

app_name = "orders"

urlpatterns = [
    path("", OrderList.as_view(), name="list"),
    path("create/", order_create, name="create"),
    path("<int:pk>/edit/", order_update, name="edit"),
    path("<int:pk>/delete/", OrderDelete.as_view(), name="delete"),
]
