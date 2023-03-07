from os import environ


class CONFIG:
    TWITTER = {
        "API_KEY": environ.get("API_KEY", ""),
        "API_SECRET_KEY": environ.get("API_SECRET_KEY", ""),
        "ACCESS_KEY": environ.get("ACCESS_KEY", ""),
        "ACCESS_SECRET": environ.get("ACCESS_SECRET", ""),
    }

    REDIS_URL = environ.get("REDIS_URL", "redis://172.17.0.1:6379")

    PORT = environ.get("PORT", 3030)

    LOOKUP_TIMEOUT = environ.get("LOOKUP_TIMEOUT", 30)

    # NOTSET - DEBUG - INFO - WARN - ERROR - CRITICAL
    LOGLEVEL = environ.get("LOGLEVEL", "INFO")

    TEST = environ.get("TEST", '')
