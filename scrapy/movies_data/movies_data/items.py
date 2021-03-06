# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviesDataItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    star = scrapy.Field()
    desc = scrapy.Field()
    writer = scrapy.Field()
    date = scrapy.Field()
    