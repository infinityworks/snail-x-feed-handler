import requests
from config import URLS
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.mappers import round_mapper
from feed.respositories import round_repository


def scheduled_round_call():

    token = get_auth_token()
    call_round_api(token)

    return "Scheduled round call"


scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_round_call(), trigger="interval", hours=12)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


#
# API FEEDS
#


def call_round_api(token):
    url = URLS['results']

    headers = {
        'Authorization': token
    }

    response = requests.get(url, headers=headers)

    response_body = response.text

    round, race_list = round_mapper.json_to_round_and_race_list(response_body)

    round_id = round_repository.save(round)

    return "Calling round api"


# AUTH

def get_auth_token():
    url = URLS['auth']
    request = requests.get(url)
    return request.text
