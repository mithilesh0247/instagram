from rest_framework import serializers
from company.models import Brand, MessageInfluencer, MessageBrand, BrandPost


class BrandRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request

    class Meta:
        model = Brand
        fields = ['company_name', 'designation', 'proof_of_employement', 'brand_name', 'company_website',
                  'brand_logo', 'industry', 'company_type', 'company_size', 'select_document', 'upload_document']


class BrandProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['company_name', 'designation',
                  'proof_of_employement', 'brand_name', 'brand_logo']


class BrandProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class InfluencerMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageInfluencer
        fields = ['msg', 'file']


class BrandMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBrand
        fields = ['msg', 'file']


class BrandPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BrandPost
        fields = ["msg", "file", "video", "add_external_links", "tag",
                  "post_type", "collaboration_with", "location", "companion_name"]
