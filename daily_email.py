from weather import get_weather
from genai_weatherman import generate_weather_commentary
from emailer import send_email

def scheduled_weather_email():
    weather = get_weather()
    forecast = generate_weather_commentary(weather)
    send_email(
        subject="Your daily weather forecast right to your email",
        body=forecast,
        to="diego.sebas2915@gmail.com",
    )