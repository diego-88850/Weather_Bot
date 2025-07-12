import os
from apscheduler.schedulers.blocking import BlockingScheduler

class WeatherScheduler:
    def __init__(self):
        self.scheduler = BlockingScheduler()

    def add_email_job(self, job_func, frequency="Daily", day_of_week='mon', hour=20, minute=53):
        if frequency == "Daily":
            trigger = "cron"
            self.scheduler.add_job(job_func, trigger=trigger, hour=hour, minute=minute)
        elif frequency == "Weekly":
            self.scheduler.add_job(job_func, trigger="cron", day_of_week=day_of_week, hour=hour, minute=minute)

    def start(self):
        print("[SCHEDULER] Starting")
        self.scheduler.start()