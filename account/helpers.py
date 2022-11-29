import requests
import random
#from Tinssleproject.settings import API_KEY
# from account.models import User
# from django.conf import settings


def send_otp_to_phone(phone_number):
    API_KEY = "a1d31489-17f6-11ed-9c12-0200cd936042"
    try:
        otp = random.randint(1000, 9999)
        print(otp)
        url = f'https://2factor.in/API/V1/{API_KEY}/SMS/{phone_number}/{otp}'
        response = requests.get(url)
        print(response)
        return otp
    except Exception as e:
        return None
# send_otp_to_phone(7903598027)
