import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.handlers import round_handler, token_handler, race_result_handler

scheduler = BackgroundScheduler()

global_inflight = False


def scheduled_round_call():
    print("Running scheduled round call")

    token_response = token_handler.call_auth_api()
    if token_response.status_code == 200:
        token = token_handler.get_auth_token_from_response(token_response.json())

        round_response = round_handler.call_round_api(token)
        round_handler.process_round_response(round_response.json(), token)
    else:
        print("API Unreachable.")


def round_inflight_check():  # Called every hour to check if a round is newly inflight
    print("round_inflight_check called!")
    global global_inflight  # Have to declare this weirdly so can access it within this method
    if not global_inflight:
        if round_handler.round_inflight():
            global_inflight = True
            print("Second scheduler running")
            scheduler.add_job(func=scheduled_race_result_call, trigger="interval", seconds=3, id='100')
        else:
            print("No round inflight!")


def scheduled_race_result_call():
    print("Schedule_race__result_call called")
    global global_inflight
    token_response = token_handler.call_auth_api()
    if token_response.status_code == 200:
        token = token_handler.get_auth_token_from_response(token_response.json())

        race_result_response = race_result_handler.call_race_result_api(token)
        round_ended = race_result_handler.process_race_result_response(race_result_response.json())
        if round_ended:
            global_inflight = False
            print("Ending round!")
            scheduler.remove_job('100')
    else:
        print("API Unreachable.")


def run_scheduler():
    scheduler.add_job(func=scheduled_round_call, trigger="interval", seconds=15)
    scheduler.add_job(func=round_inflight_check, trigger="interval", seconds=5)
    scheduler.start()
    print("Scheduler started.")

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
