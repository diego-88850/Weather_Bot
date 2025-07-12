import os
import requests
from dotenv import load_dotenv
from logger import log_event

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("BASE_URL")

def get_weather(city: str = "Detroit") -> dict:
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no",
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        log_event("weather", "success", f"Weather data retrieved for {city}")
        return response.json()
    except requests.exceptions.HTTPError as errh:
        log_event("weather", "error", str(errh))
        return {}