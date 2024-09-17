from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = Cart
        fields = ['id', 'product_name', 'quantity', 'status']
