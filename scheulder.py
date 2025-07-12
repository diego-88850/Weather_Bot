import os
from apscheduler.schedulers.blocking import BlockingScheduler

class WeatherScheduler:
    def __init__(self):
        self.scheduler = BlockingScheduler()

    def add_daily_email_job(self, job_func, hour=20, minute=53):
        self.scheduler.add_job(
            job_func,
            trigger='cron',
            hour=hour,
            minute=minute,
        )

    def start(self):
        print("[SCHEDULER] Starting")
        self.scheduler.start()