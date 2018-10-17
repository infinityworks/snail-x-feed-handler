import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.handlers import round_handler, token_handler


def scheduled_round_call():

    print("Running scheduled round call")

    token = token_handler.get_auth_token()
    round_handler.call_round_api(token)

    return "Scheduled round call"


def run_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=scheduled_round_call, trigger="interval", hours=12)
    scheduler.start()
    print("Scheduler started.")

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
