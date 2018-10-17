import requests
from config import URLS
from feed.repositories import snail_repository


def process_snail_list(snail_list, token):
    for id in snail_list:
        response = call_snail_api(id, token)
        process_snail_api_response_json(response.json())


def call_snail_api(snail_id, token):
    url = URLS['snails'] + str(snail_id)
    print(url)

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


def process_snail_api_response_json(response_json):
    snail_repository.process_snail_json(response_json)
