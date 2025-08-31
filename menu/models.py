# menu/models.py
from django.db import models
from decimal import Decimal

class MenuItem(models.Model):
    name = models.CharField(max_length=120)                 # جديد
    category = models.CharField(max_length=120, blank=True) # جديد
    price = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal("0.00"))
    image = models.ImageField(upload_to="menu/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})" if self.category else self.name
