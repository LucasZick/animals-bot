import time
import os
import signal
import logging

import tweepy
from redis import Redis

from twitterBot.MessageBuilders import RandomAnimalMessageBuilder
from twitterBot.config import CONFIG


print(CONFIG.LOGLEVEL)
logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", level=CONFIG.LOGLEVEL.upper())

def get_redis(redis_url):
    instance = Redis.from_url(redis_url)

    if not instance.ping():
        raise ConnectionError("Redis instance is down.")

    return instance


def get_twitter(api_key, api_secret_key, access_key, access_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret_key, access_key, access_secret)

    return tweepy.API(auth, wait_on_rate_limit=True)

def get_animals():
    with open("animals.txt", "r", encoding="utf8") as file:
        return list(map(lambda animal: animal.split("(")[0].strip(), file.readlines()))

def set_last_tweet(twitter_client, redis_client):
    tweet = twitter_client.mentions_timeline(count = 1)[0]
    redis_client.set("last_seen_tweet_id", tweet.id)

def main():
    redis_client = get_redis(CONFIG.REDIS_URL)
    logging.info("Connected to Redis!")
    
    twitter_client = get_twitter(CONFIG.TWITTER["API_KEY"], CONFIG.TWITTER["API_SECRET_KEY"], CONFIG.TWITTER["ACCESS_KEY"], CONFIG.TWITTER["ACCESS_SECRET"])
    logging.info("Connected to Twitter!")

    animals = get_animals()
    RandomAnimalMessageBuilder.add_animals(animals)

    while True:
        last_seen_tweet_id = redis_client.get("last_seen_tweet_id")

        if type(last_seen_tweet_id) == bytes:
            last_seen_tweet_id = int(last_seen_tweet_id.decode("utf-8")) #transform from bytes to string to, finally, integer
        else:
            set_last_tweet(twitter_client, redis_client)
            continue

        logging.info(f"Starting from Tweet ID: {last_seen_tweet_id}.")

        tweets = twitter_client.mentions_timeline(since_id=last_seen_tweet_id)
        logging.info(f"Found {len(tweets)} to reply to.")

        for tweet in reversed(tweets):
            try:
                logging.debug("Got tweet ID {tweet.id}.")
                random_animal_message = RandomAnimalMessageBuilder.build_random_animal_message()
                twitter_client.update_status(f"@{tweet.user.screen_name} {random_animal_message}", in_reply_to_status_id=tweet.id)
            except BaseException:
                logging.exception(f"Error while trying to reply to tweet ID {tweet.id}.")
            finally:
                redis_client.set("last_seen_tweet_id", tweet.id)

        time.sleep(int(CONFIG.LOOKUP_TIMEOUT))

def run():
    try:
        main()
    except BaseException as e:
        logging.exception(f"Your service is shutting down due to critical errors.")
        os.kill(os.getppid(), signal.SIGTERM)
        
