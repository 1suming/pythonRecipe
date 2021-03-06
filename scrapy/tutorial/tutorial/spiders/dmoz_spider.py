'''
Created on 2015-8-27
'''
#coding:utf-8
import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domains=["dmoz.org"]
    start_urls=[
                 "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
       # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self,response):

        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            #print title, link, desc
            item=DmozItem()
            item['title']=title
            item['link']=link
            item['desc']=desc
            yield item 