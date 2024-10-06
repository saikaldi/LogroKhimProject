from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Manufacturer, Product, Price
from .serializers import CategorySerializer, ManufacturerSerializer, ProductSerializer, PriceSerializer
from rest_framework.exceptions import NotFound
# Category ViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Категория была удалена."}, status=status.HTTP_200_OK)
        except NotFound:
            return Response({"message": "Категория не найдена."}, status=status.HTTP_404_NOT_FOUND)


# Manufacturer ViewSet
class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Производитель был удален."}, status=status.HTTP_200_OK)
        except NotFound:
            return Response({"message": "Производитель не найден."}, status=status.HTTP_404_NOT_FOUND)


# Product ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Продукт был удален."}, status=status.HTTP_200_OK)
        except NotFound:
            return Response({"message": "Продукт не найден."}, status=status.HTTP_404_NOT_FOUND)


# Price ViewSet (For creating price inquiries)
class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({"message": "Цена была удалена."}, status=status.HTTP_200_OK)
        except NotFound:
            return Response({"message": "Цена не найдена."}, status=status.HTTP_404_NOT_FOUND)