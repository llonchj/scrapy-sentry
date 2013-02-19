import os

from scrapy.conf import settings

from raven import Client

SENTRY_DSN = os.environ.get("SENTRY_DSN", None)

def get_client(dsn=None):
    if dsn is None:
        dsn = settings.get("SENTRY_DSN", SENTRY_DSN)
    return Client(dsn)
