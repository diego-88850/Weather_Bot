from scheulder import WeatherScheduler
from daily_email import scheduled_weather_email
from logger import init_db, log_event
from preferences import get_preferences

def main():
    init_db()

    city, time, day_of_week, frequency, personality, email_address = get_preferences()
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    ws = WeatherScheduler()
    ws.add_email_job(
        scheduled_weather_email(city, personality, email_address),
        day_of_week,
        frequency,
        hour,
        minute
    )
    if not all([time, email_address, city]):
        log_event("main", "ERROR", "Missing user preferences. Cannot start scheduler.")
        return
    ws.start()

if __name__ == "__main__":
    main()