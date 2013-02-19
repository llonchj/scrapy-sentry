"""
Send signals to Sentry

Use SENTRY_DSN setting to enable sending information
"""
import logging

from scrapy import signals, log
from scrapy.mail import MailSender
from scrapy.exceptions import NotConfigured

from raven import Client

class Sentry(object):
    def __init__(self, stats, client=None, dsn=None):
        self.client = client if client else Client(dsn)
        
    @classmethod
    def from_crawler(cls, crawler, client=None, dsn=None):
        dsn = crawler.settings.get("SENTRY_DSN")

        client = Client(dsn)

        o = cls(crawler.stats, client=client, dsn=dsn)

        sentry_signals = crawler.settings.get("SENTRY_SIGNALS", [])
        if len(sentry_signals):
            for signal in sentry_signals:
                if isinstance(signal, basestring):
                    signal = getattr(signals, signal, None)
                #elif isinstance(signal, [tuple, list]):
                #    name = signal[0]
                #    args = signal[1:]
                #   signal = getattr(signals, name, None)

                receiver = o.signal_receiver
                #if receiver is None:
                #    print "RECEIVER IS NONE", o, dir(o)

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
        
        ident = self.client.get_ident(
            self.client.capture('Message', message=message, extra=extra))
        return ident

