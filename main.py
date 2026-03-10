from weather import get_weather
from news import get_news

def run_pipeline():
    print("Running Data Pipeline...")

    weather = get_weather()
    news = get_news()
    
    print("Today's Weather:")
    print(weather)
    print("\nToday's News:")
    print(news)

run_pipeline()