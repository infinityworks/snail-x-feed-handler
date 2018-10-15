import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from feed.handlers import handler


def scheduled_round_call():

    token = handler.get_auth_token()
    handler.call_round_api(token)

    return "Scheduled round call"


scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_round_call(), trigger="interval", hours=12)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
