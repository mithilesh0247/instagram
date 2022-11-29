import jwt
# Create your views here.
from django.conf import settings
from django.conf import settings
import jwt
import json


def user_token_data(token, request):
    token = request.META.get('HTTP_AUTHORIZATION')
    token1 = token.split()
    token2 = token[7::]
    token3 = "".join(token2)
    decoded = jwt.decode(token3, settings.SECRET_KEY, algorithms=["HS256"])
    user_id = decoded['user_id']
    print(user_id)

    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTE3ODU1LCJpYXQiOjE2NjAxMTQyNTUsImp0aSI6ImM0ZTE1MTkwNjdiNTQzNTg4MjFmZjc5M2VmMThiYTI3IiwidXNlcl9pZCI6M30.SUssXfBbN6al9r_FXBSH4cTT9mUThcyK52-8H2e3y28"

    print(user_token_data(request, token)
          )
