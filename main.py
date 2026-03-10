from weather import get_weather
from news import get_news

def run_pipeline():
    weather = get_weather()
    news = get_news()

    # parse weather
    city = weather["name"]
    temp = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    description = weather["weather"][0]["description"]
    humidity = weather["main"]["humidity"]

    # display weather
    print("\n" + "="*50)
    print("GOOD MORNING")
    print("="*50)
    print(f"\n📍 Weather in {city}")
    print(f"   {temp}°F — {description.capitalize()}")
    print(f"   Feels like {feels_like}°F | Humidity {humidity}%")

    # display news
    print("\n📰 TOP HEADLINES")
    print("-"*50)
    for article in news[:5]:  # just top 5 for now
        source = article["source"]["name"]
        title = article["title"]
        print(f"\n  [{source}]")
        print(f"  {title}")

    print("\n" + "="*50)

run_pipeline()