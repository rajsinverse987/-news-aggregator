from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity

    if score > 0.1:
        sentiment = "Positive"
    elif score < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, round(score, 2)