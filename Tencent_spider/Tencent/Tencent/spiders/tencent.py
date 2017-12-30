# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

        for node in node_list:
            # 每一个item表示一个职位信息
            item = TencentItem()
            item["position_name"] = node.xpath(".//a/text()").extract_first()
            item["position_link"] = node.xpath(".//a/@href").extract_first()
            item["position_type"] = node.xpath("./td[2]/text()").extract_first()
            item["people_number"] = node.xpath("./td[3]/text()").extract_first()
            item["work_location"] = node.xpath("./td[4]/text()").extract_first()
            item["publish_times"] = node.xpath("./td[5]/text()").extract_first()

            yield item

        # 使用与确定的页码，一直循环判断并自增
        # 优点是写法简单，缺点是并没有用到scrapy的并发
        if self.offset <= 2690:
            self.offset += 10
            # callback 表示回调函数
            # 请求发送出去，返回的响应由callback指定定的方法解析
            yield scrapy.Request(url=self.base_url + str(self.offset), callback=self.parse)