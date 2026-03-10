from flask import Flask, render_template, request
from weather import get_weather
from news import get_news
from bias_analysis import analyze_bias
from database import init_db, save_weather, save_articles, save_analysis

app = Flask(__name__)

# initialize database when app starts
init_db()


@app.route("/")
def home():
    city = request.args.get("city", "New York")
    topic = request.args.get("topic", "top stories")

    # guard against empty city
    if not city.strip():
        city = "New York"

    weather = get_weather(city)

    # check if weather API returned an error
    if weather.get("cod") != 200:
        city = "New York"
        weather = get_weather(city)

    weather_data = {
        "city": weather["name"],
        "temp": weather["main"]["temp"],
        "feels_like": weather["main"]["feels_like"],
        "description": weather["weather"][0]["description"].capitalize(),
        "humidity": weather["main"]["humidity"]
    }

    headlines = get_news(topic=topic)
    analysis = analyze_bias(headlines)

    # parse articles
    articles = []
    for article in headlines[:10]:
        articles.append({
            "source": article["source"]["name"],
            "title": article["title"].split(" - ")[0],
            "description": article["description"],
            "url": article["url"],
            "published_at": article.get("publishedAt", "")
        })

    # save everything to database
    save_weather(weather_data)
    save_articles(articles)
    save_analysis(analysis)

    return render_template("index.html",
                         weather=weather_data,
                         articles=articles,
                         analysis=analysis,
                         city=city,
                         topic=topic)

if __name__ == "__main__":
    app.run(debug=True)