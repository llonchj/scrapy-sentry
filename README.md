scrapy-sentry
=============

Logs Scrapy exceptions into Sentry

A python library that glues [Sentry](http://www.getsentry.com) with [Scrapy](http://www.scrapy.org).


Requisites: 
-----------

* [Sentry server](http://www.getsentry.com/)

Installation
------------

  ```
  pip install scrapy-sentry
  ```

Setup
-----

Use the provided middleware, add to your Scrapy Project `settings.py` file:

  ```
  # sentry dsn
  SENTRY_DSN = 'http://public:secret@example.com/1'
  EXTENSIONS = {
      #
      # log spider_errors to sentry.
      "scrapy_sentry.extensions.Errors":10,
  }

  ```

Example Project
---------------
Try the example project.

  ```
  env SENTRY_DSN="http://example.com/1" scrapy crawl example
