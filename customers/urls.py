# customers/urls.py
from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("", views.CustomerList.as_view(), name="list"),
    path("create/", views.CustomerCreate.as_view(), name="create"),
    path("<int:pk>/edit/", views.CustomerUpdate.as_view(), name="edit"),
    path("<int:pk>/delete/", views.CustomerDelete.as_view(), name="delete"),
]
