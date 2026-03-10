import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_news(topic="top stories"):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}&pageSize=20&language=en&sortBy=publishedAt"
    
    response = requests.get(url)
    data = response.json()
    
    return data["articles"]

get_news()

