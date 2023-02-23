from os import environ


class CONFIG:
    TWITTER = {
        "API_KEY": environ.get("API_KEY", ""),
        "API_SECRET_KEY": environ.get("API_SECRET_KEY", ""),
        "ACCESS_KEY": environ.get("ACCESS_KEY", ""),
        "ACCESS_SECRET": environ.get("ACCESS_SECRET", ""),
    }

    REDIS_URL = environ.get("REDIS_URL", False)

    PORT = environ.get("PORT", False)

    LOOKUP_TIMEOUT = environ.get("LOOKUP_TIMEOUT", 5)

    LOGLEVEL = environ.get("LOGLEVEL", "INFO")

    DEBUG = environ.get("DEBUG", False)
