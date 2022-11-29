from django.shortcuts import render
import jwt
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from Influencer.models import Influencer, InfluencerPost
from Influencer.models import InfluencerPost as InfluencerPostModel
from django.conf import settings
from .serializers import InfluencerRegistrationSerializer, InfluencerStorySerializer, InfluencerProfileSerializer, InfluencerProfileUpdateSerializer, InfluencerPostSerializer, InfluencerPostDetailSerializer, InfluencerPostUpdateSerializer, InfluencerFollowSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from yaml import serialize
from account.models import User
from account.views import get_tokens_for_user
from account.renderers import InfluencerRenderer
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
import jwt
import json
from django.db.models import Q


class InfluencerRegistration(APIView):
    def post(self, request, format=None):
        serializer = InfluencerRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ss = serializer.save()
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)
        user = User.objects.filter(id=user_id).update(
            user_type='Influencer', user_type_id=ss.id)
        return Response({"msg": "Influencer Data Is Saved SuccessFully"})


class InfluencerProfileView(APIView):
    renderer_classes = [InfluencerRenderer]
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

        influencer_profile = Influencer.objects.get(id=sss)
        serializer = InfluencerProfileSerializer(influencer_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfluencerProfileUpdateView(APIView):
    renderer_classes = [InfluencerRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request):
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
        influencer_profile_update = Influencer.objects.get(id=sss)
        serializer = InfluencerProfileUpdateSerializer(
            influencer_profile_update, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Influencer Update Their profile:"})


class InfluencerPost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        c_data = request.data
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
        print(sss)
        Influencer_data = Influencer.objects.get(id=sss)
        sender_name = Influencer_data.first_name + Influencer_data.last_name
        post_type = c_data.get("post_type")
        if post_type not in ['collaboration', 'paid promotion']:
            c_data["post_type"] = "normal"
        c_data['sender'] = sender_name
        c_data['post_type_id'] = user_id
        post_count = InfluencerPostModel.objects.filter(
            post_type_id=user_id)
        print(post_count)
        serializer = InfluencerPostSerializer(data=c_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            "data": serializer.data,
            "msg": "Influencer Post save Successfully"
        }
        return Response(data, status=status.HTTP_200_OK)


class InfluencerPostDetailView(APIView):
    renderer_classes = [InfluencerRenderer]
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
        post_data = InfluencerPostModel.objects.all()
        serializer = InfluencerPostDetailSerializer(post_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InfluencerPostUpdateView(APIView):
    renderer_classes = [InfluencerRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request):
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
        post_data = InfluencerPostModel.objects.filter(post_type_id=sss)
        print(post_data)
        my_data = post_data.values_list()
        print(my_data)
        return Response({"msg": "Influencer Post Update Successfully:"})


class Influencerfollow(APIView):
    renderer_classes = [InfluencerRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        ss = User.objects.get(id=user_id)
        sss = ss.user_type_id
        f_data = Influencer.objects.get(id=sss)
        aa = f_data.follow
        data = request.data
        aa.append(data['follow_id'])
        print(aa)
        p = Influencer.objects.update(follow=f_data.follow)
        return Response({"msg": "Influencer follow this user:"})


class InfluencerFollowList(APIView):
    renderer_classes = [InfluencerRenderer]

    def get(request, self, format=None):
        ff = Influencer.objects.filter(Q(main_content_category='Fahion') | Q(
            main_content_category='Lifestyle') | Q(main_content_category='DIY'))
        ki = []
        for user in ff:
            data = {
                "user_id": user.id,
                "user_name": user.first_name,
                "user_main_content_category": user.main_content_category,
                # "user_email": user.email,
                # "user_phone_number": user.phone_number,
                # "user_password": user.password,
            }
            ki.append(data)
        return Response({"data": ki, "msg": "Influencer Data:"})


class InfluencerStoryView(APIView):
    renderer_classes = [InfluencerRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        token = token.split()
        str1 = ""
        for ch in token:
            str1 = str1+ch
        str2 = str1.replace("Bearer", '')
        decoded = jwt.decode(str2, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded["user_id"]
        print(user_id)

        # ss = User.objects.get(id=user_id)
        # print(ss.user_type)
        return Response({'msg': "Influencer Story save !"})
