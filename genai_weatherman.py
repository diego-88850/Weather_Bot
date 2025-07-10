import os
from http.client import responses

import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()
client.api_key = os.getenv("GENAI_API_KEY")

def generate_weather_commentary(weather_data: dict, persona: str = "cheerful weatherman") -> str:
    city = weather_data["location"]["name"]
    temp = weather_data["current"]["temp_f"]
    condition = weather_data["current"]["condition"]["text"]
    wind = weather_data["current"]["wind_mph"]
    uv_index = weather_data["current"]["uv"]

    prompt = (
        f"Here is the city: {city}, Temperature: {temp}°F, Condition: {condition}, Wind Speed: {wind} mph, uv index: {uv_index}"
        f"Give me a forecast based on this type of persona: {persona}, make sure to be creative and stay friendly"
    )

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"[Error generating weather commentary] {e}"