# -*- coding: utf-8 -*-

# Scrapy settings for ImagesPipelineUse project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ImagesPipelineUse'

SPIDER_MODULES = ['ImagesPipelineUse.spiders']
NEWSPIDER_MODULE = 'ImagesPipelineUse.spiders'


ITEM_PIPELINES = { 'ImagesPipelineUse.MyImagesPipeline.MyImagesPipeline'
                   #'scrapy.contrib.pipeline.images.ImagesPipeline': 1
                }

IMAGES_STORE='E:/img'
IMAGES_THUMBS = {
            'small':(50, 50),


}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ImagesPipelineUse (+http://www.yourdomain.com)'
