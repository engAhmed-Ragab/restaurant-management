# customers/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm

class CustomerList(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

class CustomerCreate(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

class CustomerUpdate(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customers:list")

class CustomerDelete(DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customers:list")
