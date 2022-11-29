from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Influencer.models import Influencer
from Influencer.models import InfluencerPost as InfluencerPostModel, InfluencerStory


class InfluencerRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registration Request

    class Meta:
        model = Influencer
        fields = ['first_name', 'last_name', 'date_of_birth', 'city', 'state', 'country', 'platform', 'other', 'region_of_influence',
                  'monetizing_audience', 'monthly_earnings', 'audience', 'audience_age_range', 'main_content_category']


class InfluencerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = "__all__"


class InfluencerProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = ['first_name', 'last_name',
                  'date_of_birth', 'city', 'state', 'country']


class InfluencerPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = InfluencerPostModel
        fields = "__all__"


class InfluencerPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerPostModel
        fields = "__all__"


class InfluencerPostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerPostModel
        fields = ["msg", "file", "video", "add_external_links", "tag",
                  "post_type", "collaboration_with", "location", "companion_name"]


class InfluencerFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = "follow_id"


class InfluencerStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerStory
        fields = ['user_type', 'image']
