# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils.response import get_base_url
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['www.btdidi.com']
    start_urls = ['http://www.btdidi.com/search/b-5beo5aSn/1-2.html']

    def parse(self, response):
        urls = response.css("#wall .search-item .item-title h3 a::attr(href)").extract()
        for url in urls:
            base_url = get_base_url(response)
            print(parse.urljoin(base_url, url))
