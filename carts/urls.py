from django.urls import path, include
from rest_framework.routers import DefaultRouter
from carts.views import CartViewSet

router = DefaultRouter()
router.register(r'carts', CartViewSet, basename='carts')


urlpatterns = [
    path('', include(router.urls)),
]
