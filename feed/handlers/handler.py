import requests
from config import URLS
from feed.repositories import round_repository


def call_round_api(token):

    url = URLS['rounds']

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    response_json = response.json()

    round_id, race_list = round_repository.process_round_json(response_json)

    if round_id and race_list:
        print("process races")
        # process races
    else:
        print("no new round to process")


# AUTH

def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    token = request.json()['token']
    return token
