import random
from rest_framework import serializers
from users.models import User
from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': False},
            'email': {'required': True},
            'password': {'required': True},
        }

    def validate(self, data):
        password = data.get('password')
        if len(password) <= 6:
            raise serializers.ValidationError('Пароль должен состоять не менее чем из 6 символов.')
        return data

    def create(self, validated_data):
        confirmation_code = str(random.randint(1000, 9999))

        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data.get('last_name', ''),
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False,
            confirmation_code=confirmation_code
        )


        send_mail(
            'Код подтверждения по электронной почте',
            f'Ваш код подтверждения - {confirmation_code}',
            'noreply@yourdomain.com',   #email of sender
            [user.email],
            fail_silently=False  # Не игнорировать ошибки при отправке
        )

        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class EmailConfirmationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=4)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError('Неверный адрес электронной почты.')

        if user.confirmation_code != data['confirmation_code']:
            raise serializers.ValidationError('Неверный код подтверждения.')

        # Активируем пользователя
        user.is_active = True
        user.confirmation_code = None
        user.save()

        return data
