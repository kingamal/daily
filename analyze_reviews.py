import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_reviews():
    file_path = 'reviews.csv'
    reviews = pd.read_csv(file_path)

    sia = SentimentIntensityAnalyzer()

    def classify_sentiment(text):
        score = sia.polarity_scores(text)['compound']
        if score >= 0.05:
            return 'positive'
        elif score <= -0.05:
            return 'negative'
        else:
            return 'neutral'

    reviews['sentiment'] = reviews['review'].apply(classify_sentiment)

    avg_ratings = reviews.groupby('sentiment')['rating'].mean()

    print("\nAverage Ratings by Sentiment:")
    print(avg_ratings)

    print("\nSentiment Analysis Summary:")
    print(reviews)
    print(sia.polarity_scores("Wouldn't buy again. Poor quality."), 'here')

if __name__ == '__main__':
    analyze_reviews()
