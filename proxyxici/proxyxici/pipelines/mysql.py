# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class MySQLStorePipeline(object):
    def __init__(self, settings):
        self.settings = settings
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                                            db=settings.get('MYSQL_DB'),
                                            user=settings.get('MYSQL_USER'),
                                            passwd=settings.get('MYSQL_PASSWORD'),
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset='utf8',
                                            use_unicode=False
                                            )

    @classmethod
    def from_settings(cls, settings):
        return cls(settings)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls.from_settings(settings)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        if item.get('proxy_ip'):
            tx.execute(
                'insert into proxy (proxy_ip,proxy_port,proxy_location,proxy_type,proxy_security) values (%s, %s, %s, %s, %s)'
                , (item['proxy_ip'], item['proxy_port'], item['proxy_location'], item['proxy_type'],
                   item['proxy_security']))
