from django.contrib import admin
from .models import Cart

@admin.register(Cart)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'status', 'added_at')

