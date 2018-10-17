import requests
from config import URLS
from feed.repositories import round_repository
from feed.handlers import race_handler


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
        race_handler.process_race_list(race_list, token)
    else:
        print("no new round to process")
