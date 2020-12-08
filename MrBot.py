from nohut import *
import tweepy
from time import sleep
import os
from os import environ

query = ("#ai OR #datascience OR #Artificialintellegence")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, 
   consumer_secret)
auth.set_access_token(access_token, 
    access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

for tweet in tweepy.Cursor(api.search, q=query).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet the tweet
        tweet.retweet()
        print('Retweeted the tweet')

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        sleep(900)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
