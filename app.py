import time
import os

import tweepy
from redis import Redis

from getAnimal import get_random_animal


def get_redis(redis_url):
    instance = Redis.from_url(redis_url, ssl_cert_reqs=None)

    if not instance.ping():
        raise ConnectionError('Redis instance is down.')

    return instance


def get_twitter(api_key, api_secret_key, access_key, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key, access_key, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)


def _main_():
    r = get_redis(os.environ['REDIS_URL'])
    api = get_twitter(os.environ['API_KEY'], os.environ['API_SECRET_KEY'], os.environ['ACESS_KEY'], os.environ['ACCESS_SECRET'])

    last_seen_tweet_id = str(r.get('last_seen_tweet_id'))
    tweets = api.mentions_timeline(last_seen_tweet_id, tweet_mode='extended')
    print('deu bao')
    print('Ultimo ID pesquisado:' + last_seen_tweet_id)
    for tweet in reversed(tweets):
        r.set('last_seen_id', tweet.id)
        genius_phrase = get_random_animal()
        api.update_status(f"@{tweet.user.screen_name} {genius_phrase}", in_reply_to_status_id=tweet.id)


while True:
    _main_()
    time.sleep(60)
