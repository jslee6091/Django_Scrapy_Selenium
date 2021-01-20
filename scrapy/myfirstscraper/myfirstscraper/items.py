# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    title = scrapy.Field()
    score = scrapy.Field()
    review = scrapy.Field()
    writer = scrapy.Field()
    date = scrapy.Field()