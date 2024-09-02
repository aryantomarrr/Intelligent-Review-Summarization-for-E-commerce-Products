from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Dict

def analyze_sentiments(reviews: List[str]) -> List[Dict[str, float]]:
    sia = SentimentIntensityAnalyzer()
    sentiments = []
    for review in reviews:
        sentiment = sia.polarity_scores(review)
        if sentiment['compound'] >= 0.05:
            label = 'POSITIVE'
        elif sentiment['compound'] <= -0.05:
            label = 'NEGATIVE'
        else:
            label = 'NEUTRAL'
        sentiments.append({'label': label, 'score': sentiment['compound']})
    return sentiments
