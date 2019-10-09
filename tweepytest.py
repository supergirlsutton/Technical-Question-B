import tweepy
import os
import env_file

env_file.load()

API_KEY = os.environ['API_KEY']
SECRET_API_KEY = os.environ['SECRET_API_KEY']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
SECRET_ACCESS_TOKEN = os.environ['SECRET_ACCESS_TOKEN']

auth = tweepy.OAuthHandler(API_KEY, SECRET_API_KEY)
auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

api = tweepy.API(auth)

public_tweets = api.search(q="dogs filter:media -#caturday", count=50)
for tweet in public_tweets:
#	if not "#caturday" in tweet.text:
	print("https://twitter.com/supergirlsutton/status/{}".format (tweet.id), tweet.text)