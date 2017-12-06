# -*- coding: utf-8 -*-

# Scrapy settings for vDown project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'vDown'

SPIDER_MODULES = ['vDown.spiders']
NEWSPIDER_MODULE = 'vDown.spiders'



'''
ITEM_PIPELINES = { 'vDown.MyImagesPipeline.MyImagesPipeline',
                   'vDown.MyFilePipeline.MyFilePipeline',
                   #'scrapy.contrib.pipeline.images.ImagesPipeline': 1
                }

IMAGES_STORE='G:/blueSmall/img'
IMAGES_THUMBS = {
            'small':(50, 50),


}
FILES_STORE='G:/blueSmall'
'''
CLOSESPIDER_TIMEOUT=120 #超时多少就close


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vDown (+http://www.yourdomain.com)'
