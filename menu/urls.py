# menu/urls.py
from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.MenuList.as_view(), name="list"),
    path("create/", views.MenuCreate.as_view(), name="create"),
    path("<int:pk>/edit/", views.MenuUpdate.as_view(), name="edit"),
    path("<int:pk>/delete/", views.MenuDelete.as_view(), name="delete"),
]
