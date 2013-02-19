scrapy-sentry
=============

A python library that glues [Sentry](http://www.getsentry.com) with [Scrapy](http://www.scrapy.org).

Features
--------

* Allows logging of exceptions into Sentry

Requisites: 
-----------
* [Sentry server](http://www.getsentry.com)


Installation
------------

  ```
  pip install scrapy-sentry
  ```

  It is highly recommended to use UDP as SENTRY_DSN. Read on how to setup a [UDP server for Sentry](http://sentry.readthedocs.org/en/latest/udp_server/index.html).


Setup (Method 1)
----------------

Append the following code at the end of `settings.py`:

  ```
  # log into sentry
  SENTRY_DSN = 'http://public:secret@example.com/1'

  import scrapy_sentry
  scrapy_sentry.init(SENTRY_DSN)

  ```

Replace SENTRY_DSN with the right one for your project, or you can invoke scrapy with the SENTRY_DSN environment variable.

Setup (Method 2)
----------------
Use the provided middleware in `settings.py`:

  ```
  # log into sentry
  SENTRY_DSN = 'http://public:secret@example.com/1'

  SPIDER_MIDDLEWARES = {
      'scrapy_sentry.middlewares.SentryMiddleware': 10,
  }

  DOWNLOADER_MIDDLEWARES = {
      'scrapy_sentry.middlewares.SentryMiddleware': 10,
  }

  ```

Send signals to Sentry
----------------------

To send scrapt signals to Sentry, ensure a valid SENTRY_DSN is setup and 
create a list with the signals to be delivered to Sentry.

Use the `SENTRY_SIGNALS` in `settings.py`:

  ```
  SENTRY_SIGNALS = [
      'engine_started',
      'engine_stopped',
      # 'item_dropped',
      # 'item_passed',
      # 'item_scraped',
      # 'request_received',
      # 'response_downloaded',
      # 'response_received',
      # 'spider_closed',
      # 'spider_error',
      # 'spider_idle',
      # 'spider_opened',
      # 'stats_spider_closed',
      # 'stats_spider_closing',
      # 'stats_spider_opened',
  ]
  ```

Example Project
---------------
Try the example project.

  ```
  env SENTRY_DSN="http://example.com/1" scrapy crawl example
