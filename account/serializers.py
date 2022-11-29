from curses.ascii import isalpha
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import authenticate, get_user_model
from .social_auth import *
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from account.utils import Util
from account.mail import sendmail
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    username = serializers.CharField(validators=[alphanumeric])

    class Meta:
        model = User
        fields = ['email', 'name', 'password',
                  'password2', 'phone_number', 'username', 'otp', 'otptime']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Validating Password and Confirm Password while Registration
    # def validate(self, attrs):
    #     password = attrs.get('password')
    #     password2 = attrs.get('password2')
        # if password != password2:
        #     raise serializers.ValidationError(
        #         "Password and Confirm Password doesn't match")
        # return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserLoginSerializerWithUsername(serializers.ModelSerializer):
    username = serializers.CharField(validators=[alphanumeric])

    class Meta:
        model = User
        fields = ['password']


class UserLoginSerializerOtp(serializers.ModelSerializer):
    #email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['phone_number']


class UserLoginSerializerEmailOtp(serializers.ModelSerializer):
    #email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email']


class VerifyOtp(serializers.ModelSerializer):
    class Meta:
        phone_number = serializers.CharField(max_length=13)
        model = User
        fields = ['phone_number', 'otp']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phone_number']


class UserChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        user.set_password(password)
        user.save()
        return attrs


class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # name = User.objects.get(name = name)
            print(user)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded UID', uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print('Password Reset Token', token)
            link = 'http://localhost:8000/api/user/reset/'+uid+'/'+token
            body = 'Click Following Link to Reset Your Password '+link
            data = {
                'subject': 'Reset Your Password',
                'body': body,
                'to': user.email
            }

            print('Password Reset Link', link)
            sendmail(data)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Registered User')

            # Send EMail


class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        max_length=255, style={'input_type': 'password'}, write_only=True)

    class Meta:
        fields = ['password', 'password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError(
                    "Password and Confirm Password doesn't match")
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError(
                    'Token is not Valid or Expired')
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user, token)
            raise serializers.ValidationError('Token is not Valid or Expired')


class SocialLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    provider = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=1000)
    # is_seller=serializers.BooleanField(read_only=True)

    def validate(self, data):
        email = data.get('email')
        provider = data.get('provider')
        token = data.get('token')
        username = data.get('username')
        if provider is None:
            provider = "Web"
        # Raise an exception if an
        # email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if username is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # Raise an exception if a
        # password is not provided.
        if token is None:
            raise serializers.ValidationError(
                'A token is required to log in.'
            )
        # authorizing with provider auth

        if provider == "google":
            status = GoogleAuth.authenticate(access_token=token)
        elif provider == "facebook":
            status = FacebookAuth.authenticate(access_token=token)
        else:
            status = GoogleAuth.authenticate(access_token=token)

        if status:
            userModel = get_user_model()
            try:
                user = userModel.objects.get(email=email)
                created = False
            except userModel.DoesNotExist:
                user = User.objects.create(
                    username=username, email=email, provider=provider)
                created = True
            # Django provides a flag on our `User` model called `is_active`. The
            # purpose of this flag is to tell us whether the user has been banned
            # or deactivated. This will almost never be the case, but
            # it is worth checking. Raise an exception in this case.
            if not user.is_active:
                raise serializers.ValidationError(
                    'This user has been deactivated.'
                )
            return {
                'email': user.email,
                'username': user.username,
                'token': user.token,
                'provider': user.provider,
            }
        else:
            raise serializers.ValidationError(
                'Failed to authenticate the token with the given provider.'
            )
