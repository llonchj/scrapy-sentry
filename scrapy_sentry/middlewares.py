import sys

from scrapy import log
from scrapy.conf import settings

from utils import get_client

class SentryMiddleware(object):
    def __init__(self, dsn=None):
        self.client = get_client(dsn)

    @classmethod
    def from_settings(cls, settings):
        dsn = settings.get("SENTRY_DSN", None)
        return cls(dsn)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def trigger(self, exception, spider=None, extra={}):
        msg = self.client.captureException(exc_info=sys.exc_info(), extra=extra)
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

