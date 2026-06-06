from newsapi import NewsApiClient

API_KEY = "c793eab8e2954c5c83e5270ba9950a88"

def get_news(topic):
    newsapi = NewsApiClient(api_key=API_KEY)
    
    response = newsapi.get_everything(
        q=topic,
        language="en",
        sort_by="publishedAt",
        page_size=10
    )
    
    articles = []
    for article in response["articles"]:
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "source": article["source"]["name"],
            "publishedAt": article["publishedAt"]
        })
    
    return articles