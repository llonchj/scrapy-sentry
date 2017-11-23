# -*- coding: utf-8 -*-
 
from scrapy import Spider

class NitidumSpider(Spider):

    name = 'example'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost/']

    def parse(self, response):
      raise Exception("this is an exception in the spider")
