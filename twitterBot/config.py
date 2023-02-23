from os import environ


class CONFIG:
    TWITTER = {
        "API_KEY": environ.get("API_KEY", ""),
        "API_SECRET_KEY": environ.get("API_SECRET_KEY", ""),
        "ACCESS_KEY": environ.get("ACCESS_KEY", ""),
        "ACCESS_SECRET": environ.get("ACCESS_SECRET", ""),
    }

    REDIS_URL = environ.get("REDIS_URL") if environ.get("REDIS_URL","") != "" else False

    PORT = environ.get("PORT") if environ.get("PORT", "") != "" else False

    LOOKUP_TIMEOUT = (
        environ.get("LOOKUP_TIMEOUT") if environ.get("LOOKUP_TIMEOUT", "") != "" else 5
    )

    LOGLEVEL = environ.get("LOGLEVEL") if environ.get("LOGLEVEL", "") != "" else "INFO"

    DEBUG = environ.get("DEBUG") if environ.get("DEBUG", "") != "" else False
