import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.handlers import round_handler, token_handler, race_result_handler


def scheduled_round_call():
    print("Running scheduled round call")

    token_response = token_handler.call_auth_api()
    if token_response.status_code == 200:
        token = token_handler.get_auth_token_from_response(token_response.json())

        round_response = round_handler.call_round_api(token)
        round_handler.process_round_response(round_response.json(), token)
    else:
        print("API Unreachable.")

def scheduled_race_result_call():
    token_response = token_handler.call_auth_api()
    if token_response.status_code == 200:
        token = token_handler.get_auth_token_from_response(token_response.json())

        race_result_response = race_result_handler.call_race_result_api(token)
        race_result_handler.process_race_result_response(race_result_response.json(), token)
    else:
        print("API Unreachable.")

def run_scheduler():
    scheduler = BackgroundScheduler()
    # scheduler.add_job(func=scheduled_round_call, trigger="interval", hours=12)
    if (round_handler.round_inflight()):
        scheduler.add_job(func=scheduled_race_result_call, trigger="interval", seconds=20)
    scheduler.add_job(func=scheduled_race_result_call, trigger="interval", seconds=20)
    scheduler.start()
    print("Scheduler started.")

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
