from weather import get_weather
from news import get_news
from bias_analysis import analyze_bias

def run_pipeline():
    weather = get_weather()
    news = get_news()
    analysis = analyze_bias(news)

    # weather display
    city = weather["name"]
    temp = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    description = weather["weather"][0]["description"]
    humidity = weather["main"]["humidity"]

    print("\n" + "="*50)
    print("🌅  GOOD MORNING — DAILY DIGEST")
    print("="*50)
    print(f"\n📍 Weather in {city}")
    print(f"   {temp}°F — {description.capitalize()}")
    print(f"   Feels like {feels_like}°F | Humidity {humidity}%")

    # headlines display
    print("\n📰 TOP HEADLINES")
    print("-"*50)
    for article in news[:5]:
        source = article["source"]["name"]
        title = article["title"].split(" - ")[0]
        print(f"\n  [{source}]")
        print(f"  {title}")

    # bias analysis display
    print("\n🤖 AI BIAS ANALYSIS")
    print("-"*50)
    print(analysis)
    print("\n" + "="*50)

run_pipeline()