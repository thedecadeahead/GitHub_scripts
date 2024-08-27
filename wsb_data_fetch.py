import requests
from textblob import TextBlob

REDDIT_API_URL = "https://www.reddit.com/r/wallstreetbets/top/.json?limit=100&t=day"

def get_wsb_sentiment(symbol):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(REDDIT_API_URL, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch WSB data: {response.status_code}")
        return 0  # Neutral sentiment if failed to fetch data
    
    posts = response.json().get('data', {}).get('children', [])
    symbol_mentions = [post for post in posts if symbol.upper() in post['data']['title'].upper()]

    sentiment_scores = []
    for post in symbol_mentions:
        blob = TextBlob(post['data']['selftext'])
        sentiment_scores.append(blob.sentiment.polarity)

    if sentiment_scores:
        return sum(sentiment_scores) / len(sentiment_scores)
    else:
        return 0  # Neutral sentiment if no relevant posts

def adjust_prediction_with_wsb_sentiment(symbol, prediction_probability):
    wsb_sentiment = get_wsb_sentiment(symbol)
    adjusted_prediction = prediction_probability + (wsb_sentiment * 0.2)  # Adjust prediction based on WSB sentiment
    return min(max(adjusted_prediction, 0), 1)  # Ensure between 0 and 1