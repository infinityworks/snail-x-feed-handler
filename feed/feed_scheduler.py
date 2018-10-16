import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.handlers import handler


def scheduled_round_call():

    print("Running scheduled round call")

    # token = handler.get_auth_token()
    # handler.call_round_api(token)

    return "Scheduled round call"


def run_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=scheduled_round_call, trigger="interval", seconds=12)
    scheduler.start()
    print("Scheduler started.")

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
