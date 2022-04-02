import time
import os
import signal
import logging

import tweepy
from redis import Redis

from MessageBuilders import RandomAnimalMessageBuilder


logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=os.environ.get('LOGLEVEL', 'INFO').upper())

def get_redis(redis_url):
    instance = Redis.from_url(redis_url, ssl_cert_reqs=False)

    if not instance.ping():
        raise ConnectionError('Redis instance is down.')

    return instance


def get_twitter(api_key, api_secret_key, access_key, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key, access_key, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)

def get_animals():
    with open('animals.txt', 'r', encoding="utf8") as file:
        return list(map(lambda animal: animal.split('(')[0].strip(), file.readlines()))

def main():
    redis_client = get_redis(os.environ['REDIS_URL'])
    logging.info('Connected to Redis!')

    twitter_client = get_twitter(os.environ['API_KEY'], os.environ['API_SECRET_KEY'], os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
    logging.info('Connected to Twitter!')

    animals = get_animals()
    RandomAnimalMessageBuilder.add_animals(animals)

    while True:
        last_seen_tweet_id = int(redis_client.get('last_seen_tweet_id'))
        logging.info(f"Starting from Tweet ID: {last_seen_tweet_id}.")

        tweets = twitter_client.mentions_timeline(since_id=last_seen_tweet_id)
        logging.info(f"Found {len(tweets)} to reply to.")

        for tweet in reversed(tweets):
            try:
                logging.debug('Got tweet ID {tweet.id}.')
                random_animal_message = RandomAnimalMessageBuilder.build_random_animal_message()
                twitter_client.update_status(f"@{tweet.user.screen_name} {random_animal_message}", in_reply_to_status_id=tweet.id)
            except BaseException as e:
                logging.exception(f"Error while trying to reply to tweet ID {tweet.id}.")
            finally:
                redis_client.set('last_seen_tweet_id', tweet.id)

        time.sleep(int(os.environ['LOOKUP_TIMEOUT']))

def run():
    try:
        main()
    except BaseException as e:
        logging.exception(f"Your service is shutting down due to critical errors.")
        os.kill(os.getppid(), signal.SIGTERM)
        
