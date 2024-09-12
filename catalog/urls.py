from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import CategoryViewSet, ManufacturerViewSet, ProductViewSet, PriceViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'prices', PriceViewSet, basename='price')

urlpatterns = [
    path('', include(router.urls)),
]
