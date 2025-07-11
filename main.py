from scheulder import WeatherScheduler
from daily_email import scheduled_weather_email

def main():
    ws = WeatherScheduler()
    ws.add_daily_email_job(scheduled_weather_email)
    ws.start()

if __name__ == "__main__":
    main()