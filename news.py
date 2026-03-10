import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news():
    api_key= os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8b9755bf1eec4801aff0ba55e7130b3d"

    response = requests.get(url)
    data = response.json()

    print(data)

get_news()

