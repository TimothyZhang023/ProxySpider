# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ProxyxiciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_id = Field()
    fetch_time = Field()
    url = Field()

    pass


class ProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    proxy_ip = Field()
    proxy_port = Field()
    proxy_location = Field()
    proxy_security = Field()
    proxy_type = Field()

    pass
