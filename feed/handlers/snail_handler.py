import requests
from config import URLS
from feed.repositories import snail_repository, racecard_repository


# Cycles through a list of snails and calls API for each id
def process_snail_list(race_id, snail_list, token):
    for snail_id in snail_list:
        response = call_snail_api(snail_id, token)
        process_snail_api_response_json(response.json())
    racecard_repository.write_racecard_data(race_id, snail_list)


# Calls the API for the snails and returns a response body
def call_snail_api(snail_id, token):
    url = URLS['snails'] + str(snail_id)

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_snail_api_response_json(response_json):
    snail_repository.process_snail_json(response_json)
