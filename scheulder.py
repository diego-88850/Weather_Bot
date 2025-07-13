import os
from apscheduler.schedulers.blocking import BlockingScheduler

class WeatherScheduler:
    def __init__(self):
        self.scheduler = BlockingScheduler()

    def add_email_job(self, job_func, frequency="daily", day_of_week="monday", hour=1, minute=1):
        if frequency == "daily":
            trigger = "cron"
            self.scheduler.add_job(job_func, trigger=trigger, hour=hour, minute=minute)
        elif frequency == "weekly":
            self.scheduler.add_job(job_func, trigger="cron", day_of_week=day_of_week, hour=hour, minute=minute)

    def start(self):
        print("[SCHEDULER] Starting")
        self.scheduler.start()