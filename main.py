from scheulder import WeatherScheduler
from daily_email import scheduled_weather_email
from logger import init_db, log_event

def main():
    init_db()

    ws = WeatherScheduler()
    ws.add_daily_email_job(scheduled_weather_email)
    ws.start()

if __name__ == "__main__":
    main()