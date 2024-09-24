from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from .forms import SendNotificationForm
from django.core.mail import send_mail

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

    actions = ['send_email_to_all_users', 'send_email_to_selected_users']

    def send_email_to_all_users(self, request, queryset):
        if 'apply' in request.POST:
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipient_emails = [user.email for user in User.objects.all()]
                send_mail(subject, message, 'ukyzsaikal@gmail.com', recipient_emails)
                self.message_user(request, "Уведомление успешно отправлено всем пользователям.")
                return None
        else:
            form = SendNotificationForm()

        return render(request, 'admin/send_notification_form.html', {'form': form})

    def send_email_to_selected_users(self, request, queryset):
        if 'apply' in request.POST:
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                recipient_emails = [user.email for user in queryset]
                send_mail(subject, message, 'ukyzsaikal@gmail.com', recipient_emails)
                self.message_user(request, "Уведомление успешно отправлено выбранным пользователям.")
                return None
        else:
            form = SendNotificationForm()

        return render(request, 'admin/send_notification_form.html', {'form': form})

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
