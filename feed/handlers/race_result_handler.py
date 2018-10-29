import requests
from config import URLS
from feed.repositories import race_result_repository


# Calls results api and returns results json response
def call_race_result_api(token):
    url = URLS['results']

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_race_result_response(response):
    round_ended = race_result_repository.process_race_result_json(response)
    return round_ended
