import requests
from config import URLS
from feed.handlers import snail_handler
from feed.repositories import race_repository, racecard_repository


# Cycles through the race list to trigger API calls on each race id
def call_api_for_race_list(race_list, token):
    for id in race_list:
        response = call_race_api(id, token)
        snail_list = process_race_response_json(response.json())
        if snail_list:
            racecard_repository.write_racecard_data(id, snail_list)
            snail_handler.process_snail_list(snail_list, token)
            print("Finished processing snails")


# Calls the API and returns a response body
def call_race_api(id, token):
    url = URLS['races'] + str(id)

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)


# Processes responses json by saving the race and returning a list of snails to be processed
def process_race_response_json(response):
    race, snail_list = race_repository.process_race_json(response)

    if race and snail_list:
        print("Processing snails")
        return snail_list
    else:
        print("<No races to process>")
        return None
