from textblob import TextBlob

import tweepy

consumer_key = '7iLAMRGmz85ZhP1poOOaH3LZ1'
consumer_secret = 'mSMEVQ0VqRDKiwXIQpCm9vSmXXh4s5xO36avwIExWCsh1oTUru'

access_token = '968710659880968192-zWJcNKG7JkOfxVzHIWlvbpSAJTgSDyF'
access_secret = '7hc52hKoCvAqE3TJncc2eQibd0XVuCw5VNNg44FArpzp8'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Cryptocurrency')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)