from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, EmailConfirmationView, CurrentUserView, PasswordResetRequestView, PasswordResetView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('confirm-email/', EmailConfirmationView.as_view(), name='confirm-email'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
]




