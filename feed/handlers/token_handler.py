import requests
from config import URLS


def call_auth_api():
    url = URLS['auth']
    response = requests.get(url)
    return response


def get_auth_token_from_response(response):
    token = response['token']
    return token
