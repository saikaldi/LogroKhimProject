from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    confirmation_code = models.CharField(max_length=4, blank=True, null=True, verbose_name="Код подтверждения")
    is_active = models.BooleanField(default=False, verbose_name="Пользователь активен")  # Пользователь активен после

    # подтверждения email
    reset_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="Код сброса")

    # для личного кабинета
    organization_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название организации")
    legal_address = models.TextField(blank=True, null=True, verbose_name="Юридический адрес")
    physical_address = models.TextField(blank=True, null=True, verbose_name="Физический адрес")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Номер телефона")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Пользователи'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
