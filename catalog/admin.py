from django.contrib import admin
from .models import Category, Manufacturer, Product, Price

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    verbose_name = "Категория"
    verbose_name_plural = "Категории"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    verbose_name = "Производитель"
    verbose_name_plural = "Производители"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'manufacturer', 'stock_quantity', 'slug')
    list_filter = ('category', 'manufacturer', 'stock_quantity')
    prepopulated_fields = {'slug': ('name',)}
    verbose_name = "Продукт"
    verbose_name_plural = "Продукты"


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'surname', 'phone_number', 'email', 'comments', 'request_file', 'slug')
    list_filter = ('product',)
    verbose_name = "Цена"
    verbose_name_plural = "Цены"
