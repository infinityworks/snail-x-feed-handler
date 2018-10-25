import requests
from config import URLS
from feed.handlers.token_handler import call_auth_api, get_auth_token_from_response


#Calls results api and returns results json response
def call_race_result_api(token):
    url = URLS['results']

    headers = {
        'Authorization': token
    }

    return requests.get(url, headers=headers)

def process_race_result_response(response):
     race_result_repository.process_race_result_json(response)