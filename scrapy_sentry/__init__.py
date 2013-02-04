# Redirect Scrapy log messages to standard Python logger
 
from twisted.python import log

from raven.conf import setup_logging
from raven.handlers.logging import SentryHandler

def init(url):
    observer = log.PythonLoggingObserver()
    observer.start()

    handler = SentryHandler(url)
    setup_logging(handler)
