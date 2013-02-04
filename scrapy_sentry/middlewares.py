import sys

from raven import Client

from scrapy import log
from scrapy.conf import settings

SENTRY_DSN = None #defaults to os.environ["SENTRY_DSN"]

class SentryMiddleware(object):
    def __init__(self, dsn=None):
        self.client = Client(dsn)

    @classmethod
    def from_settings(cls, settings):
        dsn = settings.get("SENTRY_DSN", SENTRY_DSN)
        return cls(dsn)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def trigger(self, exception, spider=None, extra={}):
        msg = self.client.captureException(sys.exc_info(), extra=extra)
        ident = self.client.get_ident(msg)
        
        log.msg("Follow last exception in Sentry '%s'" % ident, 
            level=log.INFO, spider=spider)

        return None
        
    def process_exception(self, request, exception, spider):
        return self.trigger(exception, spider, 
            extra={"spider":spider, "request":request})

    def process_spider_exception(self, response, exception, spider):
        return self.trigger(exception, spider, 
            extra={"spider":spider, "response":response})

