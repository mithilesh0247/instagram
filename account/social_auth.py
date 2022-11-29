import requests
import twitter
import os
from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
# TODO: on success, return image url and save it to user model


class GoogleAuth(object):
    """
    Provide methods for authorizing, refreshing and revoking oauth tokens
    """
    @staticmethod
    def authenticate(access_token):
        GOOGLE_VALIDATION_URL = "https://www.googleapis.com/oauth2/v1/tokeninfo"
        response = requests.get(url=GOOGLE_VALIDATION_URL, params={
                                "access_token": access_token})
        if response.status_code == 200:
            email = response.json()["email"]
            return True
        else:
            return False


class FacebookAuth(object):
    """
    Provide methods for authorizing, refreshing and revoking oauth tokens
    """
    @staticmethod
    def authenticate(access_token):
        FACEBOOK_VALIDATION_URL = f"https://graph.facebook.com/me?access_token={access_token}"

        response = requests.get(url=FACEBOOK_VALIDATION_URL, params={
                                "access_token": access_token})
        if response.status_code == 200:
            return True
        else:
            return False


class TwitterAuthTokenVerification:
    """
    class to decode user access_token and user access_token_secret
    tokens will combine the user access_token and access_token_secret
    separated by space
    """

    @staticmethod
    def validate_twitter_auth_tokens(access_token_key, access_token_secret):
        """
        validate_twitter_auth_tokens methods returns a twitter
        user profile info
        """
        consumer_api_key = 'j5LR8vP8DB77sc0eMpLpmgMcH'
        consumer_api_secret_key = 'mw9TLBPRkFnXu5TsOeQzBTZN4n3sPPUb0UPBeMmCXXo0zWb4z6'

        try:
            api = twitter.Api(
                consumer_key=consumer_api_key,
                consumer_secret=consumer_api_secret_key,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret
            )

            user_profile_info = api.VerifyCredentials(include_email=True)
            return user_profile_info.__dict__

        except Exception as identifier:

            raise serializers.ValidationError({
                "tokens": ["The tokens are invalid or expired"]})
# Google_client_id=1040127136030-8o8i3uhft9f6nvmc2fcdu0spot31kogq.apps.googleusercontent.com
# your_client_secret=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
# twitter API KEYS# 4HnVe7rPy4aU4QiUoRJxrQ1uH
# API Key Secret#yawE6HiAsfpEETFEgxuz268IOIV53YPwZOjvMy290708GTuSrJ
# twitter Bearer Token #AAAAAAAAAAAAAAAAAAAAAL1YfgEAAAAA8x1abxP5Aibd3xbTrm7UcWqA16c%3DVQ9DiWUEPMgbWMGf9TrL2a9BZUqWp2WidSkgbWg77OK74745X7
