# -*- coding: utf-8 -*-

from scrapy import Spider


class ExampleSpider(Spider):

    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/']

    def parse(self, response):
        raise Exception("this is an exception in the spider")
