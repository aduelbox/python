# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BtdidiItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    create_time = scrapy.Field()
    size = scrapy.Field()
    magnet = scrapy.Field()
