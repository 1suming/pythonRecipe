# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantopmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    name=scrapy.Field() #电影名称
    year=scrapy.Field() #上映年份
    score=scrapy.Field()#分数
    vote=scrapy.Field() #平价人数
    
    
