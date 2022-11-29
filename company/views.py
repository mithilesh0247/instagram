from django.contrib.auth import get_user_model
import base64
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
import jwt
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from company.models import Brand
from company.models import BrandPost as BrandPostModel
from django.conf import settings
from company.serializers import BrandRegistrationSerializer, BrandProfileUpdateSerializer, BrandMessageSerializer, InfluencerMessageSerializer, BrandPostSerializer, BrandProfileSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from yaml import serialize
from account.models import User
from account.views import get_tokens_for_user
from account.renderers import BrandRenderer
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from company.models import Brand, MessageBrand, MessageInfluencer
import jwt

from Influencer.models import Influencer
import json


class BrandRegistration(APIView):
    def post(self, request, format=None):
        serializer = BrandRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ss = serializer.save()
        print(ss)
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        user = User.objects.filter(id=user_id).update(
            user_type='Brand', user_type_id=ss.id)
        return Response({"msg": "Brand Data Is Saved SuccessFully"})


class BrandProfileView(APIView):
    renderer_classes = [BrandRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id

        brand_profile = Brand.objects.get(id=sss)
        serializer = BrandProfileSerializer(brand_profile)
        data = {
            "data": serializer.data,
        }

        return Response({"data": data, "msg": "Brand Profile Display Successfully: "})


class BrandProfileUpdateView(APIView):
    renderer_classes = [BrandRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request):

        # ss=serializer.save()
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        brand_data = Brand.objects.get(id=sss)
        serializer = BrandProfileUpdateSerializer(brand_data, request.data)
        if serializer.is_valid():
            serializer.save()

        return Response({"msg": "Brand Data is Partially Updatyed !"})


class InfluencerMessageView(APIView):
    renderer_classes = [BrandRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = InfluencerMessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # ss=serializer.save()
        token = request.META.get('HTTP_AUTHORIZATION')
        token1 = token.split()
        token2 = token[7::] 
        token3 = "".join(token2)
        decoded = jwt.decode(token3, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded['user_id']
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        influencer_id = Influencer.objects.get(id=sss)
        sender_name = influencer_id.first_name
        print(sender_name)
        sender_id = influencer_id.id
        sender1 = MessageInfluencer.objects.update(sender=sender_name)
        return Response({"Hello Influencer": "How are You"})


class BrandMessageView(APIView):
    def get(self, request):
        request = self.request
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        brand_id = Brand.objects.get(id=sss)
        sender_name = brand_id.company_name
        print(sender_name)
        sender2 = MessageBrand.objects.update(sender=sender_name)
        print(brand_id)
        return Response({"Hello Brand": "How are You"})


class BrandPost(APIView):
    def post(self, request, format=None):
        b_data = request.data
        post_type = b_data.get("post_type")
        if post_type not in ['collaboration', 'paid promotion']:
            b_data["post_type"] = "normal"
        serializer = BrandPostSerializer(data=b_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        token = request.META.get('HTTP_AUTHORIZATION')
        token1 = token.split()
        token2 = token[7::]
        token3 = "".join(token2)
        decoded = jwt.decode(token3, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded['user_id']
        print(user_id)
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        print(sss)
        c_name = Brand.objects.get(id=sss)
        sender_name = c_name.company_name
        print(sender_name)
        sender1 = BrandPostModel.objects.update(sender=sender_name)

        return Response({"msg": "Brand  Post save Successfully:"})
