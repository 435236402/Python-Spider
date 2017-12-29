# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名
    name = 'baidu'
    # 允许当前爬虫爬取的域名范围
    allowed_domains = ['baidu.com']

    # 第一批请求的url地址
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print len(response.body)
