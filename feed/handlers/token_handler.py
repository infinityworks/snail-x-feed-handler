import requests
from config import URLS


# Calls the auth api and returns a body
def call_auth_api():
    url = URLS['auth']
    response = requests.get(url)
    return response


# Extracts token from the response
def get_auth_token_from_response(response):
    token = response['token']
    return token
