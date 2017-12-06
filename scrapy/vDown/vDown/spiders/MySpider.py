#coding:utf-8
'''
Created on 2015-11-14
'''
import scrapy
import urllib2
import sys
import urllib

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

import re

from vDown.items import MyItem

class MovieSpider(CrawlSpider):
    name='vDown'
    allowed_domains=['91porn.it']
    searchText='我'
    start_urls=['http://www.91porn.it/search?search_query='+urllib.quote(searchText)+'&search_type=videos']
    rules=[
           #Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
           #Rule(LinkExtractor(allow=(r'class=\"well well-sm[\s\S]*?href=\"(\S+?)\"[\s\S]*?img[\s]src=\"(\S+?)\"')),callback='parse_item'),
           #Rule(LinkExtractor(allow=(r'http://www.91porn.it/video/\d+"')),callback='parse_item')
           Rule(LinkExtractor(allow=(r'/video/\d+/"')),callback='parse_item')
           
    ]
    count=2
    
    def parse_item(self,response):
        item=MyItem()
        item['url']=response.url
        
        print(response.url)
        
        videoPat=r'\<video[\s\S]*?poster=\"(\S+?)\"[\s\S]*\<source\s+src=\"(\S+?)\"';
        
        m=re.match(videoPat,response.body)
        print(m.groups())
        
        #item['file_urls']=response.xpath("//img/@src").extract()
        return item