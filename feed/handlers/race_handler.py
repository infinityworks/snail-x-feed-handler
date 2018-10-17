import requests
from config import URLS
from feed.handlers import snail_handler
from feed.repositories import race_repository


def process_race_list(race_list, token):
    for id in race_list:
        call_race_api(id, token)


def call_race_api(id, token):
    url = URLS['races'] + str(id)

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    response_json = response.json()

    race, snail_list = race_repository.process_race_json(response_json)

    if race and snail_list:
        print("process snails")
        snail_handler.process_snail_list(snail_list, token)
    else:
        print("no races to process")
