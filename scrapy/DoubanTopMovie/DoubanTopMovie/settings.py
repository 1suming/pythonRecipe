# -*- coding: utf-8 -*-

# Scrapy settings for DoubanTopMovie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DoubanTopMovie'

SPIDER_MODULES = ['DoubanTopMovie.spiders']
NEWSPIDER_MODULE = 'DoubanTopMovie.spiders'

ITEM_PIPELINES={
               'DoubanTopMovie.pipelines.DoubanmoivePipeline':400
             }
COOKIES_ENABLED = True

CLOSESPIDER_TIMEOUT=120 #超时多少就close

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DoubanTopMovie (+http://www.yourdomain.com)'
