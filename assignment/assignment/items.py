# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    Name = scrapy.Field()
    URL = scrapy.Field()
    Images = scrapy.Field()
    Price = scrapy.Field()
    Sizes = scrapy.Field()
