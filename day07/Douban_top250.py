# -*- coding:utf-8 -*-

import requests
from Queue import Queue
from lxml import etree
import time


class Douban(object):
    def __init__(self):
        self.url_list = ['https://movie.douban.com/top250?start=' + str(num) for num in range(0, 250, 25)]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 添加队列
        self.data_queue = Queue()

    def send_request(self, url):
        response = requests.get(url=url,headers=self.headers)
        self.parse_page(response)

    def parse_page(self, response):
        html_obj = etree.HTML(response.content)
        node_list = html_obj.xpath("//div[@class='info']")

        for node in node_list:
            # 电影标题
            title = node.xpath("./div[@class='hd']/a/span/text()")[0]
            # 电影评价
            score = node.xpath(".//span[@class='rating_num']/text()")[0]
            # 添加到队列
            self.data_queue.put(title + '\t' + score)

    def start_work(self):
        for url in self.url_list:
            self.send_request(url)

        # 判断队列是否为空
        while not self.data_queue.empty():
            # 打印队列中的信息
            print self.data_queue.get()


if __name__ == '__main__':
    start = time.time()
    spider = Douban()
    spider.start_work()
    print "[INFO]:Useing time:%f" % (time.time() - start)