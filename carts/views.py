from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cart
from catalog.models import Product
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only return the current user's cart items
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # Adding product to cart
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)

        # Filter for existing cart items with the same product and user
        cart_items = Cart.objects.filter(user=request.user, product=product, status='pending')

        if cart_items.exists():
            # If cart item already exists, update the quantity of the first item found
            cart_item = cart_items.first()
            cart_item.quantity += 1
            cart_item.save()
        else:
            # If no existing cart item, create a new one
            cart_item = Cart.objects.create(
                user=request.user,
                product=product,
                quantity=1,
                status='pending'
            )

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Update cart item quantity
        cart_item = self.get_object()
        cart_item.quantity = request.data.get('quantity', cart_item.quantity)
        cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # Remove item from cart
        cart_item = self.get_object()
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
