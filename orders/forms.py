# orders/forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer"]

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["item", "quantity", "unit_price"]

OrderItemFormSet = inlineformset_factory(
    Order,
    OrderItem,
    form=OrderItemForm,
    fields=["item", "quantity", "unit_price"],
    extra=1,
    can_delete=True,
)
