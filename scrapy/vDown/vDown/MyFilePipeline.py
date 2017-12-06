#coding:utf-8
'''
Created on 2015-11-14
'''
from scrapy.contrib.pipeline.files  import FilesPipeline

class MyFilePipeline(FilesPipeline):
        def file_path(self,request,response=None,info=None):
            image_guid=request.url.split('/')[-1]
            return 'full/%s' % (image_guid)