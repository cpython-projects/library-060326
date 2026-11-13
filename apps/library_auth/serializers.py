from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'gender', 'birth_date')
        read_only_fields = ('id',)

    def validate_email(self, email):
        email = email.lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("Email already exists")
        return email

    def validate(self, attrs):
        attrs_without_password = attrs.copy()
        attrs_without_password.pop('password')

        user = User(**attrs_without_password)
        password = attrs['password']

        try:
            validate_password(password, user)
        except DjangoValidationError as error:
            raise serializers.ValidationError({'password': list(error.messages)})

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'gender', 'birth_date', 'date_joined')
        read_only_fields = ('id', 'username', 'email')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate_new_password(self, new_password):
        validate_password(new_password, self.context['request'].user)
        return new_password

    def validate_old_password(self, old_password):
        user = self.context['request'].user
        if not user.check_password(old_password):
            raise serializers.ValidationError('Пароль не верно указан')
        return old_password

    def validate(self, attrs):
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        if old_password and new_password and new_password == old_password:
            raise serializers.ValidationError('Passwords the same')
        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save(update_fields=['password'])
        return user
















    def create(self, validated_data):
        return User.objects.create_user(**validated_data)