import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(lat= "40.7128", lon= "-74.0060"):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"

    response = requests.get(url)
    data = response.json()

    print(data)

get_weather()