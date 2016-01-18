import tweepy
from random import randint
from time import sleep
import ipdb
import os

##CONSUMER_KEY = 'ECmRusKhD3g5vxtu6oqDOeu3f'
##CONSUMER_SECRET = 'P35jC3qpGKRrmVQANmXhndCuD3KIEvXxy3FJdMLlTO4hraU5wr'
##ACCESS_TOKEN = '2762195401-Pp54Nr2yo1SU97EotbOEiQPWsnwlDT9YVywU0dW'
##ACCESS_TOKEN_SECRET = 'b421kMofhXWOosfKpu17yHhhLxXusBeBHoQlmSHcKzVc9'


CONSUMER_KEY = os.environ['CONSUMER_KEY'] 
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

count=0

global uid 
uid = 0
a = api.mentions_timeline()

uid = a[0].id
##while(True):

    ##firstTweet = api.search("dogs")[0]
    ##firstTweet = api.home_timeline()
    ##if firstTweet.id==temp:
    ##    sleep(randint(10,20))
    ##    continue

    ##rid=firstTweet.id
    ##rsn=firstTweet.user.screen_name
while(True):
	sleep(5)
	mention = api.mentions_timeline(uid)
	print "Mention lenght = %d" %(len(mention))
	for i in api.mentions_timeline(uid):
		m = "@%s Hello Mr. %s" %(i.user.screen_name, i.user.name)
		#ipdb.set_trace()
		api.update_status(status=m, in_reply_to_status_id=i.user.id)
		#ipdb.set_trace()
		uid = i.id
		print uid
		#count=count+1
		#print(count)
	#temp = firstTweet.id
