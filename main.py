import time
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

from logger import logger_object
from scheduler import heartbeat_job, reminder_job, startup_job


def main():
    scheduler = BackgroundScheduler()

    scheduler.add_job(heartbeat_job, trigger='interval', seconds=10)
    scheduler.add_job(reminder_job, trigger='interval', minutes=1)

    run_time = datetime.now() + timedelta(seconds=30)
    scheduler.add_job(startup_job, trigger='date', run_date=run_time)

    scheduler.start()
    logger_object.info("Scheduler started. Running for 2 minutes...")

    try:
        time.sleep(120)
    finally:
        scheduler.shutdown()
        logger_object.info("[SHUTDOWN] Scheduler stopped. All jobs completed.")


if __name__ == "__main__":
    main()
    