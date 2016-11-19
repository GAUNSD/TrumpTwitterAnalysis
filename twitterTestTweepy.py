import tweepy
from tweepy import OAuthHandler



CONSUMER_KEY	= 'bryJRbMnsfueCbVT58bJTrxhB'
CONSUMER_SECRET = 'GAA2jsTu5MVMcaPriv3xF9NZS7svnBdWU1R9uroA1yHKEmtOAj'
ACCESS_KEY 		= '30057519-VD9nl7OStjZfci1pawSCykmAsFXRctvapgFhGJ6rI'
ACCESS_SECRET 	= 'ma7SdTt6MtyU5XuvdgxjKbkhg4beSzY8qsH8p1gWjOPlB'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text