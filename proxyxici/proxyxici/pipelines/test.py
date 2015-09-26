__author__ = 'TianShuo'
# !/usr/bin/python
# -*-coding:utf-8-*-

from scrapy import log


class PrintProxyInfoPipeline(object):
    def __init__(self, settings):
        self.settings = settings
        pass

    @classmethod
    def from_settings(cls, settings):
        return cls(settings)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls.from_settings(settings)

    def process_item(self, item, spider):
        proxy_ip = item['proxy_ip']
        proxy_port = item['proxy_port']
        proxy_location = item['proxy_location']
        proxy_type = item['proxy_type']
        proxy_security = item['proxy_security']

        print "Got " + proxy_security + " " + proxy_type + " proxy:" + proxy_ip + ":" + proxy_port + " @" + proxy_location

        return item

    def handle_error(self, e):
        log.err(e)
