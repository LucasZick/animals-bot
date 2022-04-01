from os import read, write
import tweepy
import time
from getAnimal import getRandomAnimal
from tokens import api_key, api_secret_key, access_key, access_secret

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api.create_friendship('zickecody')