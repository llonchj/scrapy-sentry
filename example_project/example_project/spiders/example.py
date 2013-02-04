# -*- coding: utf-8 -*-
 
from scrapy.spider import BaseSpider

class NitidumSpider(BaseSpider):

    name = 'example'
    allowed_domains = ['localhost']
    start_urls = ['http://localhost/']

    def parse(self, response):
      raise Exception("this is an exception in the spider")
