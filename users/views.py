from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserRegistrationSerializer, UserSerializer, PasswordResetRequestSerializer, \
    PasswordResetSerializer, UserUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView
from users.serializers import EmailConfirmationSerializer
from django.http import HttpResponse
from .utils import send_email_to_all_users, send_email_to_user



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)  # Set user as inactive initially
            # Email sending is handled in the serializer
            return Response({'message': 'Пользователь создан успешно. Пожалуйста, подтвердите ваш email.'}, status=201)
        return Response(serializer.errors, status=400)
    def list(self, request):
        queryset = User.objects.filter(is_active=True)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User.objects.filter(is_active=True), pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(User.objects.filter(is_active=True), pk=pk)
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь успешно обновлен'})
        return Response(serializer.errors, status=400)
    #
    def destroy(self, request, pk=None):
        user = get_object_or_404(User.objects.filter(is_active=True), pk=pk)
        user.delete()
        return Response({'message': 'Пользователь успешно удален'})
    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if not user.is_active:
                raise AuthenticationFailed('Электронная почта не подтверждена.')

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

class PasswordResetRequestView(APIView):
    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Код сброса пароля отправлен на ваш email.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def notify_all_users(request):
    subject = 'Уведомление'
    message = 'Это уведомление для всех пользователей'
    send_email_to_all_users(subject, message)
    return HttpResponse('Notification sent to all users.')

def notify_user(request, user_email):
    subject = 'Уведомление'
    message = 'Это уведомление для выбранных пользователей'
    send_email_to_user(user_email, subject, message)
    return HttpResponse(f'Уведомление отправлено пользователю {user_email}.')
