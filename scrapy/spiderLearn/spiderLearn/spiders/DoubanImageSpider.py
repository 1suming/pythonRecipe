#coding:utf-8 
'''
Created on 2015-8-28
'''

import scrapy
import urllib2
import sys

from spiderLearn.DoubanImageItem import DoubanImageItem

class DoubanImageSpider(scrapy.Spider):
    name="DoubanImageSpider"
    allowed_domains=['douban.com']
    start_urls=[
                #'http://movie.douban.com/subject/1474243/photos?type=S'
                'http://movie.douban.com/celebrity/1274491/photos/'
            ]
    
    
    
    page=0
    count=0
    title=''
    
    def parse(self,response):
        self.page += 1
        self.count=0
        items=[]
        
        self.title=response.xpath("//title/text()").extract()[0].strip().replace(' ', '_')
        imagesUrls=response.xpath("//ul/li/div/a/img/@src").extract()
        for imgUrl in imagesUrls:
            originImgUrl=imgUrl.replace('thumb','photo') #raw不行
            
            item=DoubanImageItem()
            item['address']=originImgUrl
            items.append(item)
            
            self.count+=1
            self.download(originImgUrl,self.title,self.page,self.count)
            #print originImgUrl,"\n"
        #sys.exit()
        
        nextPage=response.xpath("//div[@class='paginator']/span[@class='next']/a/@href").extract()
        if(len(nextPage) ==0):
            return DoubanImageItem()
        else:
            nextPageStr=nextPage[0]
            return scrapy.Request(nextPageStr,callback=self.parse)
    
    
    def download(self,url,title,page,count):
        try:
            u=urllib2.urlopen(url,None,timeout=10)
            r=u.read()
            savePath='E://img/yanzi/%s_%d_%d.%s' % (title,page,count,url.split('.')[-1])
            print 'Downloading ... ',savePath
            downloadFile=open(savePath,'wb')
            downloadFile.write(r)
            u.close()
            downloadFile.close()
        except:
            print 'save path Failed!!!'                
            
        

