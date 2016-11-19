from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

cKey	= 'bryJRbMnsfueCbVT58bJTrxhB'
cSecret	= 'GAA2jsTu5MVMcaPriv3xF9NZS7svnBdWU1R9uroA1yHKEmtOAj'
aToken	= '30057519-VD9nl7OStjZfci1pawSCykmAsFXRctvapgFhGJ6rI'
aSecret	= 'ma7SdTt6MtyU5XuvdgxjKbkhg4beSzY8qsH8p1gWjOPlB'

class listener(StreamListener):

	def on_data(self, data):
		print data
		return True
	def on_error(self, status):
		print status

auth = OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)

twitterStream = Stream(auth, listener())

twitterStream.filter(track=["car"])


