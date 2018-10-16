import requests
from config import URLS
from feed.mappers import round_mapper
from feed.models.round import Round
from feed.repositories import round_repository
import json


def call_round_api(token):

    url = URLS['rounds']

    print(url)

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    print(response)

    round = Round(3, "Test", "Mon, 01 Oct 2018 10:00:00 GMT", "Mon, 01 Oct 2018 12:00:00 GMT")

    print(round)
    round_repository.save(round)

    # response_body = response.json()

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
    return round


# AUTH

def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    token = request.json()['token']
    return token
