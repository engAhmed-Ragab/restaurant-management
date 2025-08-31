# menu/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import MenuItem


class MenuList(ListView):
    model = MenuItem
    template_name = "menu/menu_list.html"
    context_object_name = "items"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(category__icontains=q)
            )
        return qs


class MenuCreate(CreateView):
    model = MenuItem
    template_name = "menu/menu_form.html"
    fields = "__all__"
    success_url = reverse_lazy("menu:list")


class MenuUpdate(UpdateView):
    model = MenuItem
    template_name = "menu/menu_form.html"
    fields = "__all__"
    success_url = reverse_lazy("menu:list")


class MenuDelete(DeleteView):
    model = MenuItem
    template_name = "menu/menu_confirm_delete.html"
    success_url = reverse_lazy("menu:list")
