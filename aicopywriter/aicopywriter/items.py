# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AicopywriterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_poster = scrapy.Field()
    movie_summary = scrapy.Field()
    movie_synopsis = scrapy.Field()
    movie_genre = scrapy.Field()
    movie_tagline = scrapy.Field()
