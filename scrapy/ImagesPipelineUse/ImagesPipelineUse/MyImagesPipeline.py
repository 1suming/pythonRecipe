#coding:utf-8
'''
Created on 2015-9-9
'''
from scrapy.contrib.pipeline.images import ImagesPipeline

class MyImagesPipeline(ImagesPipeline):
        def file_path(self,request,response=None,info=None):
            image_guid=request.url.split('/')[-1]
            return 'full/%s' % (image_guid)
        
    