# -*- coding: utf-8 -*-
import re
from pyspider.libs import log
import scrapy
import BeautifulSoup
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule, CrawlSpider

from scrapy.selector import HtmlXPathSelector
from proxyxici.items import ProxyItem
from proxyxici.utils.url_tool import clean_url
from scrapy.http import Request


class XiciSpider(scrapy.Spider):
    name = "xici"

    allowed_domains = ["www.xici.net.co"]
    disallowed_domains = []

    start_urls = (
        'http://www.xici.net.co',
    )

    # start_urls = (
    # 'http://www.xici.net.co/nn/',
    # 'http://www.xici.net.co/wn/',
    # 'http://www.xici.net.co/wt/',
    # 'http://www.xici.net.co/nt/',
    # )

    rules = [
        Rule(SgmlLinkExtractor(allow=(r'/([wnt]+)/?\d*',)), callback='parse_item', follow=True),
    ]

    item_patt = re.compile(r"http://www.xici.net.co/([wnt]+)/?\d*")

    def parse(self, response):
        self.log('now parse:' + response.url)

        response_selector = HtmlXPathSelector(text=response.body.decode("UTF-8", "ignore"))
        ip_list_tables = response_selector.xpath('//*[@id="ip_list"]').extract()
        for ip_list_table in ip_list_tables:
            soup = BeautifulSoup.BeautifulSoup(ip_list_table)
            for table in soup.findAll('table'):
                for row in table.findAll('tr'):
                    td_list = row.findAll('td')
                    if len(td_list) > 0:
                        proxy_ip = td_list[1].text  # ip
                        proxy_port = td_list[2].text  # port
                        proxy_location = td_list[3].text  # location
                        proxy_security = td_list[4].text  # security
                        proxy_type = td_list[5].text  # type

                        # process to pipline
                        proxy_item = ProxyItem()
                        proxy_item['proxy_ip'] = proxy_ip
                        proxy_item['proxy_port'] = proxy_port
                        proxy_item['proxy_location'] = proxy_location
                        proxy_item['proxy_type'] = proxy_type
                        proxy_item['proxy_security'] = proxy_security
                        yield proxy_item

        response_selector = HtmlXPathSelector(text=response.body)
        all_url_list = response_selector.xpath('//a/@href').extract()

        for next_link in all_url_list:
            next_link = clean_url(response.url, next_link, response.encoding)
            matched_next_link = self.item_patt.findall(next_link)
            if len(matched_next_link) == 1:
                yield Request(url=next_link, callback=self.parse_item)
                # else:
                #     yield Request(url=next_link, callback=self.parse)

        pass

    def parse_item(self, response):
        self.log('now parse_detail:' + response.url)

        response_selector = HtmlXPathSelector(text=response.body.decode("UTF-8", "ignore"))
        ip_list_tables = response_selector.xpath('//*[@id="ip_list"]').extract()
        for ip_list_table in ip_list_tables:
            soup = BeautifulSoup.BeautifulSoup(ip_list_table)
            for table in soup.findAll('table'):
                for row in table.findAll('tr'):
                    td_list = row.findAll('td')
                    if len(td_list) > 0:
                        proxy_ip = td_list[2].text  # ip
                        proxy_port = td_list[3].text  # port
                        proxy_location = td_list[4].text  # location
                        proxy_security = td_list[5].text  # security
                        proxy_type = td_list[6].text  # type
                        # proxy_speed = td_list[7].findAll(title=True)[0]['title']
                        # proxy_connection_time = td_list[8].findAll(title=True)[0]['title']
                        # proxy_vertify_time = td_list[9].text  # time

                        # process to pipline
                        proxy_item = ProxyItem()
                        proxy_item['proxy_ip'] = proxy_ip
                        proxy_item['proxy_port'] = proxy_port
                        proxy_item['proxy_location'] = proxy_location
                        proxy_item['proxy_type'] = proxy_type
                        proxy_item['proxy_security'] = proxy_security
                        yield proxy_item

        response_selector = HtmlXPathSelector(text=response.body)
        all_url_list = response_selector.xpath('//a/@href').extract()

        for next_link in all_url_list:
            next_link = clean_url(response.url, next_link, response.encoding)
            matched_next_link = self.item_patt.findall(next_link)
            if len(matched_next_link) == 1:
                yield Request(url=next_link, callback=self.parse_item)
            else:
                yield Request(url=next_link, callback=self.parse)
                # pagination_div = response_selector.xpath('//*[@id="body"]/div[@class="pagination"]').extract()[0]
                # soup = BeautifulSoup.BeautifulSoup(pagination_div)
                # next_urls = soup.findAll('a')
                # for new_url in next_urls:
                #     next_url = clean_url(response.url, new_url['href'], response.encoding)
                #     yield Request(url=next_url, callback=self.parse_item)
