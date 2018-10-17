import requests
from config import URLS
from feed.repositories import snail_repository


# Cycles through a list of snails and calls API for each id
def process_snail_list(snail_list, token):
    for id in snail_list:
        response = call_snail_api(id, token)
        process_snail_api_response_json(response.json())


# Calls the API for the snails and returns a response body
def call_snail_api(snail_id, token):
    url = URLS['snails'] + str(snail_id)

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_snail_api_response_json(response_json):
    snail_repository.process_snail_json(response_json)
