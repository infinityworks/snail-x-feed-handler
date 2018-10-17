import threading

from feed import *
from feed import feed_scheduler


# Starts the feed scheduled on a new thread to run parallel to the app
def start_scheduler():
    thread = threading.Thread(target=feed_scheduler.run_scheduler)
    thread.start()


if __name__ == '__main__':
    start_scheduler()
    app.run()
