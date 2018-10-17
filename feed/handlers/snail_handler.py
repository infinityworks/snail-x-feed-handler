import requests
from config import URLS
from feed.repositories import snail_repository


def process_snail_list(snail_list, token):
    for id in snail_list:
        call_snail_api(id, token)


def call_snail_api(snail_id, token):

    url = URLS['snails'] + str(snail_id)
    print(url)

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    response_json = response.json()

    snail_repository.process_snail_json(response_json)
