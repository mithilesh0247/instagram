from datetime import date, datetime
import email
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from yaml import serialize
from account.serializers import SendPasswordResetEmailSerializer, UserLoginSerializerWithUsername, UserLoginSerializerEmailOtp, UserChangePasswordSerializer, UserLoginSerializer, UserPasswordResetSerializer, UserProfileSerializer, UserRegistrationSerializer, SocialLoginSerializer, UserLoginSerializerOtp, VerifyOtp
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.views.generic import TemplateView
from account.helpers import send_otp_to_phone
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import User
from account.social_auth import FacebookAuth
# Generate Token Manually
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth import get_user_model
from account.emailotp import sendmail
from django.contrib.auth.hashers import make_password, check_password
from passlib.hash import pbkdf2_sha256
import random


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):

    def post(self, request, format=None):
        password = request.data.get("password")
        password2 = request.data.get("password2")
        if password != password2:
            return Response({"msg": "Password do not match pls retype "})

        request.data['password'] = make_password(request.data.get('password'))
        request.data['password2'] = make_password(
            request.data.get('password2'))
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = request.data.get('phone_number')
        otp = send_otp_to_phone(phone_number)
        time = datetime.now().strftime("%y/%m/%d,%H:%M:%S")
        print(make_password(request.data.get('password')))
        print(str(serializer))
        user = serializer.save()
        # user.password = make_password(request.data.get('password'))
        user.otp = otp
        user.otptime = datetime.now()
        user = serializer.save()

        user.save()
        token = get_tokens_for_user(user)
        return Response({"token": token, "msg": "Registration Success"})


class UserLoginWithName(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializerWithUsername(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        print(username, password)
        print(username, password)
        data = User.objects.get(username=username)
        email = data.email
        print(email)
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)

            return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserLoginWithEmailOtpView(APIView):
    def post(self, request, formate=None):
        u_data = request.data
        email = u_data['email']
        otp = random.randint(1000, 9999)
        print(otp)

        u = User.objects.filter(email=email).update(emailotp=otp)

        print(email, otp)
        body = 'Your One Time Password is:'+str(otp)
        data = {
            'subject': 'Login by Using This OTP',
            'body': body,
            'to': email,
        }
        sendmail(data)

        return Response({"msg": "otp is send at your email pls check and conform:"})


class EmailOtpVerifyView(APIView):
    def post(self, request):
        email = request.data['email']
        otp = request.data['otp']
        uu = User.objects.get(email=email)
        if uu.emailotp == otp and email == email:
            token = get_tokens_for_user(uu)
            return Response({"msg": "Login Success", "token": token}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Something went wrong!"})


class UserLoginWithOtp(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializerOtp(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.data.get('phone_number')
        e = User.objects.get(phone_number=phone_number)
        otp = send_otp_to_phone(phone_number)

        e.otp = otp
        e.otptime = datetime.now()

        otpgeneratetime = e.otptime
        e.otp = otp
        e.otptime = datetime.now()
        e.save()

        return Response({'msg': "Otp is send to the number pls verify at the login time"})


class UserVerifyOtp(APIView):
    def post(self, request, format=None):
        serializer = VerifyOtp(data=request.data)

        serializer.is_valid(raise_exception=True)

        phone_number = serializer.data.get("phone_number")
        print(phone_number)
        otp = serializer.data.get("otp")
        print(otp)
        u = User.objects.get(phone_number=phone_number)
        print(u)
        print(u.otp)
        otpgeneratetime = u.otptime
        print(otpgeneratetime)
        d4 = datetime.timestamp(datetime.fromisoformat(otpgeneratetime))+200000
        print(d4)
        d5 = datetime.timestamp(datetime.now())
        print(d5)
        print(u.otp)
        # user=authenticate(phone_number=phone_number,otp=otp)
        print(u.otp == otp)
        print(d4 <= d5)
        if u.otp == otp and d5 <= d4:
            token = get_tokens_for_user(u)
            return Response({"msg": "Login Success", "token": token}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Invalid Crediential and otp is expire!"})


class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        print(email)
        password = serializer.data.get('password')
        print(password)
        #data = User.objects.get(email=email)

        #print(data.email, data.password)

        # print(user)
        # if data.email == email and data.password == password:
        #   token = get_tokens_for_user(data)
        #  return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)

            return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(
            data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        print(email)
        return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(
            data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)


class SocialLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print(str(request.data))
        user = request.data
        if not "signup_from" in user:
            user["signup_from"] = "web"
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response('serializer.data', status=status.HTTP_200_OK)
