# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    total_review = scrapy.Field()
    ratings = scrapy.Field()
    reviewer_name = scrapy.Field()
    reviews = scrapy.Field()
    review_date = scrapy.Field()
    hash_key = scrapy.Field()
    sourceURL = scrapy.Field()
