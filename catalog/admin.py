from django.contrib import admin
from .models import Category, Manufacturer, Product, Price

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'stock_quantity', 'available_status', 'slug')
    list_filter = ('category', 'manufacturer', 'stock_quantity')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'surname', 'phone_number', 'email', 'comments', 'request_file', 'slug')
    list_filter = ('product',)

