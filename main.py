from scheulder import WeatherScheduler
from daily_email import scheduled_weather_email
from logger import init_db, log_event
from preferences import get_preferences, init_preferences_table

def main():
    init_db()
    init_preferences_table()

    city, time, day_of_week, frequency, personality, email_address = get_preferences()

    city = city or "New York"
    time = time or "03:55"
    frequency = frequency or "Daily"
    personality = personality or "friendly"
    email_address = email_address or "diego.sebas2915@gmail.com"
    day_of_week = day_of_week or "Monday"

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