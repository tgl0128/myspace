# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from selenium import webdriver
from scrapy.http import HtmlResponse
from time import sleep
class WangyiDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    #实例化一个浏览器对象
    def __init__(self):
        self.bro=webdriver.Chrome(executable_path="D:\pythonProject4\chromedriver.exe")

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):  #spider爬虫对象
        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        #如何获取动态加载的新闻数据
        #基于selenium获取动态加载数据
        bro=self.bro     #获取在爬虫类中定义的浏览器对象
        if request.url in spider.model_urls:
            #response    #五大板块对应的响应对象，实例化一个包含动态加载出的新闻数据
            bro.get(request.url)    #五个板块对应的url进行请求
            sleep(3)
            page_text=bro.page_source       #包含动态加载的新闻数据
            new_response=HtmlResponse(url=request.url,body=page_text,encoding="utf-8",request=request)
            return new_response
        else:
            return response    #其他请求响应对象

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

