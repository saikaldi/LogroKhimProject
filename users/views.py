# users/views.py
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import User
# from users.serializers import UserSerializer, UserRegistrationSerializer, UserUpdateSerializer
from users.serializers import UserRegistrationSerializer, UserSerializer
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import EmailConfirmationSerializer


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'Пользователь создан успешно'}, status=201)
        return Response(serializer.errors, status=400)

    def list(self, request):
        queryset = User.objects.filter(is_active=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = User.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    #
    # def update(self, request, pk=None):
    #     user = get_object_or_404(User, pk=pk)
    #     serializer = UserUpdateSerializer(user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message': 'Пользователь успешно обновлен'})
    #     return Response(serializer.errors, status=400)
    #
    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({'message': 'Пользователь успешно удален'})

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Email: {email}")  # Debugging
        print(f"Password: {password}")  # Debugging

        user = authenticate(request, username=email, password=password)

        print(f"Authenticated User: {user}")  # Debugging

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)

        return Response({'error': 'Неверные учетные данные'}, status=400)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Успешно вышли'}, status=status.HTTP_200_OK)
        except (AttributeError, ObjectDoesNotExist):
            return Response({'error': 'Нет активной сессии'}, status=status.HTTP_400_BAD_REQUEST)

class EmailConfirmationView(APIView):
    def post(self, request):
        serializer = EmailConfirmationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Электронная почта успешно подтверждена. Теперь вы можете войти в систему.'},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)