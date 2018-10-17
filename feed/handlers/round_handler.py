import requests
from config import URLS
from feed.repositories import round_repository
from feed.handlers import race_handler


# Queries the Round API from eternal team and returns a response object
def call_round_api(token):
    url = URLS['rounds']

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


# Process the round response json by extracting out the round to save and then process the races
def process_round_response(response_json, token):
    round_id, race_list = round_repository.process_round_json(response_json)

    if round_id and race_list:
        print("Processing races")
        race_handler.call_api_for_race_list(race_list, token)
        print("Finished processing races")
    else:
        print("<No new round to process>")
