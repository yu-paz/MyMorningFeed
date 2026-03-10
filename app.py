from flask import Flask, render_template
from weather import get_weather
from news import get_news
from bias_analysis import analyze_bias

app = Flask(__name__)

@app.route("/")
def home():
    weather = get_weather()
    news = get_news()
    analysis = analyze_bias(news)

    # parse weather
    weather_data = {
        "city": weather["name"],
        "temp": weather["main"]["temp"],
        "feels_like": weather["main"]["feels_like"],
        "description": weather["weather"][0]["description"].capitalize(),
        "humidity": weather["main"]["humidity"]
    }

    # parse news
    articles = []
    for article in news[:10]:
        articles.append({
            "source": article["source"]["name"],
            "title": article["title"].split(" - ")[0],
            "description": article["description"],
            "url": article["url"]
        })

    return render_template("index.html", 
                         weather=weather_data, 
                         articles=articles, 
                         analysis=analysis)

if __name__ == "__main__":
    app.run(debug=True)