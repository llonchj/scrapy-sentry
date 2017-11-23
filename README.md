scrapy-sentry
=============

Logs Scrapy exceptions into Sentry

A python library that glues [Sentry](http://www.getsentry.com) with [Scrapy](http://www.scrapy.org).
Any spider errors will get pushed to Sentry. Please note that currently, exceptions anywhere else (e.g. the Scrapy pipeline)
are not being reported to Sentry.


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

Supported versions
------------------
This package works with Python 2.7, 3.4 and 3.5. It has been tested with Scrapy up to version 1.2.1.  
