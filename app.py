from os import read, write
import tweepy
import time
from getAnimal import getRandomAnimal
from tokens import api_key, api_secret_key, access_key, access_secret

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def _main_():
    read_last_seen_str = str(read_last_seen(FILE_NAME))
    tweets = api.mentions_timeline(
        read_last_seen(FILE_NAME), tweet_mode='extended')
    print('deu bao')
    print('Ultimo ID pesquisado:' + read_last_seen_str)
    for tweet in reversed(tweets):
        store_last_seen(FILE_NAME, tweet.id)
        genius_phrase = getRandomAnimal()
        api.update_status('@' + tweet.user.screen_name + ' ' +
                          genius_phrase, in_reply_to_status_id=tweet.id)


while True:
    _main_()
    time.sleep(60)
