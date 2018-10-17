import requests
from config import URLS
from feed.repositories import round_repository, snail_repository
from feed.repositories import race_repository


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
        # process races
        process_race_list(race_list, token)
    else:
        print("no new round to process")


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
        process_snail_list(snail_list, token)
        # process snails
        
    else:
        print("no races to process")


def process_snail_list(snail_list, token):
    print(snail_list)
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



# AUTH

def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    token = request.json()['token']
    return token
