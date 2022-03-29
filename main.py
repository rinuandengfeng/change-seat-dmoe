from datetime import date, datetime

import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print("tick ! the time is : %s" % datetime.now())
    os.system("python library-script.py")
    os.system("bash git.sh")


if __name__ == "__main__":
    scheduler = BackgroundScheduler()

    scheduler.add_job(tick, 'interval', seconds=180)

    scheduler.start()

    print("Press Ctrl + {0} to exit".format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(180)
            print(f"sleep! - {datetime.now()}")

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job !")