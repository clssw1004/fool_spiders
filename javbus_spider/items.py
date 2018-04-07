# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavbusSpiderItem(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    download_urls = scrapy.Field()
    cover_img = scrapy.Field()
    preview_imgs = scrapy.Field()
    actors = scrapy.Field()
