import tweepy
from time import sleep

query = ("#ai OR #datascience OR #Artificialintellegence")

# Twitter Authentication
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET'] 
ACCESS_TOKEN = environ['ACCESS_TOKEN'] 
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, 
   CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, 
    ACCESS_SECRET)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

for tweet in tweepy.Cursor(api.search, q=query).items():
    try:
        print('\nTweet by: @' + tweet.user.screen_name)

        # Favorite the tweet
        tweet.favorite()
        print('Favorited the tweet')

        sleep(30)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
