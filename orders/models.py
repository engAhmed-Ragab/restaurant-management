# orders/models.py
from django.db import models
from django.db.models import Sum, F
from customers.models import Customer
from menu.models import MenuItem

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"

    @property
    def total(self):
        # Sum of quantity * unit_price across items
        agg = self.items.aggregate(total=Sum(F("quantity") * F("unit_price")))
        return agg["total"] or 0
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ("order", "item")

    def __str__(self):
        return f"{self.item} x {self.quantity}"

    @property
    def line_total(self):
        return self.quantity * self.unit_price
