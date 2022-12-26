from textblob import TextBlob
import tweepy
import csv
import pandas as pd

api_key = '_________'
api_secret = '________'
access_token = '_________'
access_token_secret = '________'

# field names
fields = ['tweets', 'polarity', 'sentiment','source']
# writing to csv file
with open('musk-sentiments.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames = fields)
	writer.writeheader()

authentication = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret)
authentication.set_access_token(access_token, access_token_secret)

api = tweepy.API(authentication)

trend = 'elon musk'
polarity = 0
positive = 0
negative = 0
neutral = 0
tweets = 200

results = tweepy.Cursor(api.search_tweets, q=trend, lang='en').items(tweets)

for tweet in results:
    #print(tweet)
    source = tweet.source #platform source for tweet
    refined_tweet = tweet.text.replace('RT', '')
    analysis = TextBlob(refined_tweet)
    polarity += analysis.polarity
    if polarity > 0:
        positive += 1
        mood='POSITIVE'
    elif polarity < 0:
        negative += 1
        mood = 'NEGATIVE'
    else:
        neutral += 1
        mood='NEUTRAL'
    doc_details = {'tweets':[refined_tweet], 'polarity':[analysis.polarity], 'sentiment':[mood], 'source':[source]}
    df = pd.DataFrame(doc_details)
    csv_save = df.to_csv('musk-sentiments.csv', mode='a', index=False, header=False)

print(polarity)
print("Number of positive tweets:",positive)
print("Number of neutral tweets:",neutral)
print("Number of negative tweets:",negative)