from weather import get_weather
from genai_weatherman import generate_weather_commentary
from emailer import send_email

def scheduled_weather_email(city, personality, email_address):
    weather = get_weather(city)
    forecast = generate_weather_commentary(weather, personality)
    send_email(
        subject="Here's the weather forecast for today",
        body=forecast,
        to=email_address,
    )