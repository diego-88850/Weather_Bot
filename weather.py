import os
import requests
from dotenv import load_dotenv

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
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"[weather.py] Weather API call failed: {errh}")
        return {}