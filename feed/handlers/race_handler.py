import requests
from config import URLS
from feed.handlers import snail_handler
from feed.repositories import race_repository


def call_api_for_race_list(race_list, token):
    for id in race_list:
        response = call_race_api(id, token)
        snail_list = process_race_response_json(response.json())
        snail_handler.process_snail_list(snail_list, token)


def call_race_api(id, token):
    url = URLS['races'] + str(id)

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_race_response_json(response):
    response_json = response

    race, snail_list = race_repository.process_race_json(response_json)

    if race and snail_list:
        print("process snails")
        return snail_list
    else:
        print("no races to process")
        return None
