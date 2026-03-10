import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city="New York"):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    
    response = requests.get(url)
    data = response.json()
    
    return data

get_weather()