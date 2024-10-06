from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from catalog.models import Product
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show favorites for the current user
        return Favorite.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'])
    def add(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'error': 'Требуется ID продукта'}, status=400)
        product = get_object_or_404(Product, id=product_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
        if created:
            return Response({'message': 'Продукт добавлен в избранное'}, status=201)
        return Response({'message': 'Продукт уже в избранном'}, status=200)

    @action(detail=False, methods=['post'])
    def remove(self, request):
        product_id = request.data.get('product_id')
        if not product_id:
            return Response({'error': 'Требуется ID продукта'}, status=400)
        product = get_object_or_404(Product, id=product_id)
        favorite = Favorite.objects.filter(user=request.user, product=product).first()
        if favorite:
            favorite.delete()
            return Response({'message': 'Продукт удален из избранного'}, status=200)
        return Response({'error': 'Продукт не найден в избранном'}, status=404)