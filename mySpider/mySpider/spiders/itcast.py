# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class ITCastSpider(scrapy.Spider):
    # 爬虫名:必须写
    name = "itcast"
    # 允许爬虫爬取的域名范围
    allowed_domains = ["itcast.cn"]
    # 起始url地址列表，第一批请求发送的url地址
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    # 4 默认解析start_urls的响应对象
    def parse(self, response):
        # 提取所有老师的节点
        node_list = response.xpath("//div[@class='li_txt']")

        # item_list = []
        # 迭代每个老师节点，并创建item对象保存信息
        for node in node_list:
            item = MyspiderItem()
            item['name'] = node.xpath("./h3/text()").extract_first()
            item['title'] = node.xpath("./h4/text()").extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()

            yield item


"""
item_list = []

            item_list.append(item)

        # 如果需要直接存储到json、csv、xml等基本文件里，可以将所有item数据放入到列表里
        # 最后返回这个列表，那么执行命令的时候，通过-o输出到指定文件里
        return item_list
"""
