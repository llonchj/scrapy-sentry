from __future__ import absolute_import

import os
import sys

from scrapy import log
from scrapy.conf import settings  # noqa
from scrapy.exceptions import NotConfigured

from .utils import get_client


class SentryMiddleware(object):
    def __init__(self, dsn=None, client=None):
        self.client = client if client else get_client(dsn)

    @classmethod
    def from_crawler(cls, crawler):
        dsn = os.environ.get(
            "SENTRY_DSN", crawler.settings.get("SENTRY_DSN", None))
        if dsn is None:
            raise NotConfigured('No SENTRY_DSN configured')
        return cls(dsn)

    def trigger(self, exception, spider=None, extra={}):
        extra = {
            'spider': spider.name if spider else "",
        }
        msg = self.client.captureException(
            exc_info=sys.exc_info(), extra=extra)
        ident = self.client.get_ident(msg)

        l = spider.log if spider else log.msg
        l("Sentry Exception ID '%s'" % ident, level=log.INFO)

        return None

    def process_exception(self, request, exception, spider):
        return self.trigger(exception, spider,
                            extra={"spider": spider, "request": request})

    def process_spider_exception(self, response, exception, spider):
        return self.trigger(exception, spider,
                            extra={"spider": spider, "response": response})
