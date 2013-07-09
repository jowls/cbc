from scrapy.spider import BaseSpider  # , Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
#from scrapy.http import Request
from cbc.items import LinkItem
#from selenium import selenium
import time
from random import randrange


class CBCSpider(BaseSpider):
    name = "cbc"
    allowed_domains = ["cbc.ca"]
    start_urls = ["http://www.cbc.ca/nb/news/","http://www.cbc.ca/pei/news/","http://www.cbc.ca/ns/news/"]
    pipelines = ['cbc_pipe']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="mostpopulartabs"]/div/dl/dt')
        items = []
        for site in sites:
            item = LinkItem()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            #item['desc'] = "null"
            items.append(item)
        time.sleep(randrange(45, 75))
        return items