import requests
import random
from django.conf import settings

def send_otp_to_phone(phone):
    try:
        otp = random.randint(1000, 9999)
        url = "https://api.authy.com/protected/json/phones/verification/start?api_key={}&country_code=234&phone_number={}&via=sms".format(settings.AUTHY_API_KEY, phone)
        response = requests.get(url)
        if response.status_code == 200:
            return otp
        else:
            return None
    except:
        return None