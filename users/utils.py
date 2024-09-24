from django.core.mail import send_mail
from django.conf import settings
from .models import User


def send_email_to_all_users(subject, message):
    users = User.objects.all()
    recipient_list = [user.email for user in users]

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )


def send_email_to_user(subject, message, recipient_emails):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_emails,
        fail_silently=False,
    )
