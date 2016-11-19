from twython import Twython # pip install twython
import time # standard lib

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY	= 'bryJRbMnsfueCbVT58bJTrxhB'
CONSUMER_SECRET = 'GAA2jsTu5MVMcaPriv3xF9NZS7svnBdWU1R9uroA1yHKEmtOAj'
ACCESS_KEY 		= '30057519-VD9nl7OStjZfci1pawSCykmAsFXRctvapgFhGJ6rI'
ACCESS_SECRET 	= 'ma7SdTt6MtyU5XuvdgxjKbkhg4beSzY8qsH8p1gWjOPlB'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# Now we grab Trump's tweets 
twitter.verify_credentials()

