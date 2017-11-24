"""
Send signals to Sentry

Use SENTRY_DSN setting to enable sending information
"""
from __future__ import absolute_import, unicode_literals

import os
import logging

from scrapy import signals
from scrapy.exceptions import NotConfigured

from six import StringIO


from .utils import init, get_client, get_release, response_to_dict


class Log(object):
    def __init__(self, dsn=None, *args, **kwargs):
        init(dsn)

    @classmethod
    def from_crawler(cls, crawler):
        dsn = crawler.settings.get("SENTRY_DSN", None)
        if dsn is None:
            raise NotConfigured('No SENTRY_DSN configured')
        o = cls(dsn=dsn)
        return o


class Signals(object):
    def __init__(self, client=None, dsn=None, **kwargs):
        self.client = client if client else get_client(dsn)

    @classmethod
    def from_crawler(cls, crawler, client=None, dsn=None):
        dsn = crawler.settings.get("SENTRY_DSN", None)
        o = cls(dsn=dsn)

        sentry_signals = crawler.settings.get("SENTRY_SIGNALS", [])
        if len(sentry_signals):
            receiver = o.signal_receiver
            for signalname in sentry_signals:
                signal = getattr(signals, signalname)
                crawler.signals.connect(receiver, signal=signal)

        return o

    def signal_receiver(self, signal=None, sender=None, *args, **kwargs):
        message = signal
        extra = {
            'sender': sender,
            'signal': signal,
            'args': args,
            'kwargs': kwargs,
        }
        msg = self.client.capture('Message', message=message, extra=extra)
        ident = self.client.get_ident(msg)
        return ident


class Errors(object):
    def __init__(self, dsn=None, client=None, **kwargs):
        self.client = client if client else get_client(dsn, **kwargs)

    @classmethod
    def from_crawler(cls, crawler, client=None, dsn=None):
        release = crawler.settings.get("RELEASE", get_release(crawler))

        dsn = os.environ.get(
            "SENTRY_DSN", crawler.settings.get("SENTRY_DSN", None))
        if dsn is None:
            raise NotConfigured('No SENTRY_DSN configured')
        o = cls(dsn=dsn, release=release)
        crawler.signals.connect(o.spider_error, signal=signals.spider_error)
        return o

    def spider_error(self, failure, response, spider,
                     signal=None, sender=None, *args, **kwargs):
        traceback = StringIO()
        failure.printTraceback(file=traceback)

        res_dict = response_to_dict(response, spider, include_request=True)

        extra = {
            'sender': sender,
            'spider': spider.name,
            'signal': signal,
            'failure': failure,
            'response': res_dict,
            'traceback': "\n".join(traceback.getvalue().split("\n")[-5:]),
        }
        msg = self.client.captureMessage(
            message=u"[{}] {}".format(spider.name, repr(failure.value)),
            extra=extra)  # , stack=failure.stack)

        ident = self.client.get_ident(msg)

        logging.log(logging.WARNING, "Sentry Exception ID '%s'" % ident)

        return ident
