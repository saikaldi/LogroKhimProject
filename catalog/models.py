from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

# Manufacturer Model
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    article = models.CharField(max_length=255, unique=True, verbose_name="Артикул")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    stock_quantity = models.PositiveIntegerField(default=0, verbose_name="Количество на складе")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name

    def available_status(self):
        if self.stock_quantity > 0:
            return 'доступно'
        else:
            return 'недоступно'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True, verbose_name="Комментарии")
    request_file = models.FileField(upload_to='requests/', blank=True, null=True, verbose_name="Загрузить файл")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'Запрос на {self.product.name} по {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.product.name}')
        super().save(*args, **kwargs)