#coding:utf-8
'''
Created on 2015-9-3
'''
import scrapy
import urllib2
import sys


from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor



from DoubanTopMovie.DoubantopmovieItem import DoubantopmovieItem

class MovieSpider(CrawlSpider):
    name='DoubanTopMovie'
    allowed_domains=['movie.douban.com']
    start_urls=['http://movie.douban.com/top250']
    rules=[
           Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
           Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback='parse_item')
    ]
    
    def parse_item(self,response):
        item=DoubantopmovieItem()
        item['url']=response.url
        item['name']=response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year']=response.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score']=response.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['vote'] =response.xpath('//*[@id="interest_sectl"]/div/p[2]/a/span/text()').re(r'\d+')
        
        return item