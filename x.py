import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

cKey	= 'bryJRbMnsfueCbVT58bJTrxhB'
cSecret	= 'GAA2jsTu5MVMcaPriv3xF9NZS7svnBdWU1R9uroA1yHKEmtOAj'
aToken	= '30057519-VD9nl7OStjZfci1pawSCykmAsFXRctvapgFhGJ6rI'
aSecret	= 'ma7SdTt6MtyU5XuvdgxjKbkhg4beSzY8qsH8p1gWjOPlB'

auth = OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)

api = tweepy.API(auth)
page_list = []
n = 0

result = api.user_timeline('realDonaldTrump')

outFileName = raw_input("Input the name of the out file: ")
outFile = open(outFileName, "w")

outFile.write(str(result))

outFile.close()
#for status in result:
#        print status.text
