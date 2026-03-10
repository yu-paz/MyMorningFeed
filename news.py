import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news():
    sources = "cnn,fox-news,bbc-news,the-washington-post,associated-press"
    api_key= os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8b9755bf1eec4801aff0ba55e7130b3d"

    response = requests.get(url)
    data = response.json()

    return data["articles"]

get_news()

