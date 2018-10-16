import requests
from config import URLS
from feed.mappers import round_mapper
from feed.respositories import round_repository
import json


def call_round_api(token):

    url = URLS['rounds']

    print(url)

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    print(response)

    response_body = response.json()

    # get last entry, check if we have it stored
    # latest_round = response_body[:-1]
    # exists = round_repository.check_round_exists(latest_round)
    # # if we dont, process it, otherwise leave it
    # if not exists:
    #     round, race_list = round_mapper.json_to_round_and_race_list(latest_round)
    #     round_id = round_repository.save(round)
    #
    #     # process races
    # else:
    #     print("exists")
    return response_body


# AUTH

def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    token = request.json()['token']
    return token
