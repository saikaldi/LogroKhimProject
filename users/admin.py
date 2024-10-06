from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from .forms import SendNotificationForm
from django.core.mail import send_mail
from .utils import send_email_to_all_users, send_email_to_user
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')

class SendNotificationForm(forms.Form):
    subject = forms.CharField(max_length=255, label="Тема")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)

    # Define fieldsets for add and change forms
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'password')}),
    )

    actions = ['notify_all_users', 'notify_user']

    def notify_all_users(self, request, queryset):
        subject = 'Уведомление'
        message = 'Это уведомление для всех пользователей'
        send_email_to_all_users(subject, message)
        self.message_user(request, "Уведомление отправлено всем пользователям.")

    notify_all_users.short_description = "Отправить уведомление всем пользователям"
    def notify_user(self, request, queryset):
        for user in queryset:
            subject = 'Уведомление'
            message = 'Это уведомление для выбранного пользователя'
            send_email_to_user(user.email, subject, message)
        self.message_user(request, "Уведомления отправлены выбранным пользователям.")

    notify_user.short_description = "Отправить уведомление выбранным пользователя"

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
