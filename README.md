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

Setup
-----

Append the following code at the end of `settings.py`:

  ```
  # log into sentry
  SENTRY_DSN = 'http://public:secret@example.com/1'

  import scrapy_sentry
  scrapy_sentry.init(SENTRY_DSN)

  ```

Replace SENTRY_DSN with the right one for your project.
