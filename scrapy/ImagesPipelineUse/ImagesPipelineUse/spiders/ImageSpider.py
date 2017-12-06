#coding:utf-8
'''
Created on 2015-9-7
'''

import scrapy
import urllib2
import sys
 
from ImagesPipelineUse.items import MyItem

class MovieSpider(scrapy.Spider):
    name='image'
    allowed_domains=['www.douban.com']
    start_urls=['http://www.douban.com/doulist/15894/']
    
    def parse(self,response):
        item=MyItem()
        item['image_urls']=response.xpath("//img/@src").extract()
        return item
