import requests
from config import URLS
from feed.handlers.token_handler import call_auth_api, get_auth_token_from_response


#Calls results api and returns results json response
def call_results_api():
    response = call_auth_api()
    token = get_auth_token_from_response(response.json())
    url = URLS['results']

    headers = {
        'Authorization': token
    }

    results_response = requests.get(url, headers=headers)
    print(results_response.json())

call_results_api()