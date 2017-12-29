# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    # 爬虫启动的时候调用
    def open_spider(self, spider):
        self.file_name = open("itcast.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item)) + ",\n"
        self.file_name.write(content)
        # 1.通知引擎，当前item处理完毕
        # 2.如果后续还有管道处理item，item可以通过引擎再交给下个管道
        return item

    def close_spider(self, spider):
        self.file_name.close()
