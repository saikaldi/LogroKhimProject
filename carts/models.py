from django.db import models
from django.conf import settings
from catalog.models import Product


class Cart(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании одобрения'),
        ('denied', 'Отказано'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product.name} - {self.quantity} шт."
