import tweepy
from time import sleep
import ipdb
import os
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

a = api.mentions_timeline()

uid = a[0].id
while(True):
	sleep(5)
	mention = api.mentions_timeline(uid)
	print "Mention lenght = %d" %(len(mention))
	for i in api.mentions_timeline(uid):
		m = "@%s Hello Mr. %s" %(i.user.screen_name, i.user.name)
		api.update_status(status=m, in_reply_to_status_id=i.id)
		uid = i.id
		print uid
