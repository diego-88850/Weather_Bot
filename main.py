from weather import get_weather
from genai_weatherman import generate_weather_commentary

weather_data = get_weather("Detroit") # this will later be passed in by the user but have this as a default value
persona = "goofy"  # this will later be passed in by the user but have this as a default value
forecast = generate_weather_commentary(weather_data, persona)

print(forecast)