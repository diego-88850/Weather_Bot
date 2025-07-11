import os
from apscheduler.schedulers.blocking import BlockingScheduler

class WeatherScheduler:
    def __init__(self):
        self.scheduler = BlockingScheduler()

    def add_daily_email_job(self, job_func, hour=7, minute=0):
        self.scheduler.add_job('cron', hours=hour, minutes=minute)

    def start(self):
        print("[SCHEDULER] Starting")
        self.scheduler.start()