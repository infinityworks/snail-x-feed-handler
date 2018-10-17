import threading

from feed import *
from feed import feed_scheduler


def start_scheduler():
    thread = threading.Thread(target=feed_scheduler.run_scheduler)
    thread.start()


if __name__ == '__main__':
    start_scheduler()
    app.run()

