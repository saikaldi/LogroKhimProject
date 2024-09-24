from django import forms

class SendNotificationForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient_emails = forms.CharField(help_text='Введите электронные письма, разделяя запятыми', required=False)
