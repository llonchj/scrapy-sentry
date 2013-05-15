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

Add `SENTRY_DSN` and `scrapy_sentry.extensions.Errors` extension to your Scrapy Project `settings.py`.

Example:

  ```
  # sentry dsn
  SENTRY_DSN = 'http://public:secret@example.com/1'
  EXTENSIONS = {
      "scrapy_sentry.extensions.Errors":10,
  }

  ```
