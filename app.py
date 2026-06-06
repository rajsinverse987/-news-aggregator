from flask import Flask, render_template, request
from news_fetcher import get_news
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    topic = request.args.get("topic", "technology")
    
    articles = get_news(topic)
    
    results = []
    for article in articles:
        if article["title"]:
            sentiment, score = analyze_sentiment(article["title"])
            results.append({
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "source": article["source"],
                "sentiment": sentiment,
                "score": score
            })
    
    return render_template("results.html",
                           articles=results,
                           topic=topic)

if __name__ == "__main__":
    app.run(debug=True)