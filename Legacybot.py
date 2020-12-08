import tweepy
from time import sleep

query = ("#ai OR #datascience OR #Artificialintellegence")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("WjYRx31pvXGLApFJ7QyiL0kBw", 
    "8EZE9Xnkz9PtdYSEQRjMPUyCNc25VQ4ok9in5SRICFMYTp8N2I")
auth.set_access_token("935446829730291717-xM9LVHSLzgVz01pZUKGQyeyHFG8jZZb", 
    "E2zKRdxKScIDuULgMMr5932AzecKpGDi4KSZ18GXX0HZb")

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

        sleep(225)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
