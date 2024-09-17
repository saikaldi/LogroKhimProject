import random
from rest_framework import serializers
from users.models import User
from django.core.mail import send_mail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'organization_name', 'legal_address', 'physical_address', 'phone_number')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'organization_name', 'legal_address', 'physical_address', 'phone_number')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': False},
            'email': {'required': True},
            'password': {'required': True},
            'organization_name' : {'required': False},
            'legal_address' : {'required': False},
            'physical_address' : { 'required': False},
            'phone_number': {'required': False}
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
            confirmation_code=confirmation_code,
            organization_name=validated_data.get('organization_name', ''),
            legal_address=validated_data.get('legal_address', ''),
            physical_address=validated_data.get('physical_address', ''),
            phone_number=validated_data.get('phone_number', '')
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
        fields = ('first_name', 'last_name', 'email', 'organization_name', 'legal_address', 'physical_address', 'phone_number')

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.organization_name = validated_data.get('organization_name', instance.organization_name)
        instance.legal_address = validated_data.get('legal_address', instance.legal_address)
        instance.physical_address = validated_data.get('physical_address', instance.physical_address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
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

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])
        user.is_active = True
        user.confirmation_code = None
        user.save()
        return user




class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, data):
        email = data['email']
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с таким адресом электронной почты не найден.')
        return data

    def create(self, validated_data):
        email = validated_data['email']
        user = User.objects.get(email=email)
        reset_code = str(random.randint(1000, 9999))

        # Save the reset code to the user instance
        user.reset_code = reset_code
        user.save()

        send_mail(
            'Код для сброса пароля',
            f'Ваш код для сброса пароля: {reset_code}',
            'noreply@yourdomain.com',
            [email],
            fail_silently=False
        )
        return validated_data


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reset_code = serializers.CharField(max_length=4)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        reset_code = data['reset_code']
        new_password = data['new_password']
        confirm_password = data['confirm_password']

        if new_password != confirm_password:
            raise serializers.ValidationError('Пароли не совпадают.')

        try:
            user = User.objects.get(email=email, reset_code=reset_code)
        except User.DoesNotExist:
            raise serializers.ValidationError('Неверный адрес электронной почты или код сброса.')

        return data

    def create(self, validated_data):
        email = validated_data['email']
        new_password = validated_data['new_password']

        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.reset_code = None  # Clear the reset code after password reset
        user.save()
        return validated_data
