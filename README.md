scrapy-sentry
=============

A python library that glues [Sentry](http://www.getsentry.com) with [Scrapy](http://www.scrapy.org).

Features
--------

* Allows logging of exceptions into Sentry

Installation
------------

  ```
  pip install scrapy-sentry
  ```

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

Example Project
---------------
Try the example project.

  ```
  env SENTRY_DSN="" scrapy crawl example
