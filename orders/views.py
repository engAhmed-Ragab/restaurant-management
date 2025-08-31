# orders/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from .models import Order
from .forms import OrderForm, OrderItemFormSet

class OrderList(ListView):
    model = Order
    paginate_by = 10
    template_name = "orders/order_list.html"
    context_object_name = "orders"

def order_create(request):
    order = Order()
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("orders:list")
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    return render(request, "orders/order_form.html", {"form": form, "formset": formset})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        formset = OrderItemFormSet(request.POST, instance=order)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("orders:list")
    else:
        form = OrderForm(instance=order)
        formset = OrderItemFormSet(instance=order)
    return render(request, "orders/order_form.html", {"form": form, "formset": formset, "order": order})

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy("orders:list")
    template_name = "orders/order_confirm_delete.html"
