import requests
from config import URLS

def scheduled_round_call():

    token = get_auth_token()
    call_round_api(token)

    return "Scheduled round call"


def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    return request.text


def call_round_api(token):

    url = URLS['results']

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    return "Calling round api"
