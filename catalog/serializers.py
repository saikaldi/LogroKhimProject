# in products/serializers.py
from rest_framework import serializers
from catalog.models import Price

class PriceInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['product', 'name', 'surname', 'phone_number', 'email', 'comments', 'request_file']
