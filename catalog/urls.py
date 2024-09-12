from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, EmailConfirmationView, CurrentUserView, PasswordResetRequestView, PasswordResetView

router = DefaultRouter()
router.register(r'catalog', UserViewSet, basename='catalog')

urlpatterns = [
    path('', include(router.urls)),
    # path('products/', EmailConfirmationView.as_view(), name='products'),
]




