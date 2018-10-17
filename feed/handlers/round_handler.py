import requests
from config import URLS
from feed.repositories import round_repository
from feed.handlers import race_handler


def call_round_api(token):
    url = URLS['rounds']

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_round_response(response_json, token):

    round_id, race_list = round_repository.process_round_json(response_json)

    if round_id and race_list:
        print("process races")
        race_handler.call_api_for_race_list(race_list, token)
    else:
        print("no new round to process")
