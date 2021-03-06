# -*- coding:utf-8 -*-

import requests
from Queue import Queue
from lxml import etree
import time
# 多线程
#import threading

# 多进程类库里面的多线程模块 dummy
from multiprocessing.dummy import Pool


class Douban(object):
    def __init__(self):
        self.url_list = ['https://movie.douban.com/top250?start=' + str(num) for num in range(0, 250, 25)]
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 添加队列
        self.data_queue = Queue()

    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
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
        # 单线程
        """
        for url in self.url_list:
            self.send_request(url)
        """
        # 多线程
        """
        thread_list = []
        for url in self.url_list:
            thread = threading.Thread(target=self.send_request, args=[url])
            thread.start()  # 调用线程对象里面的run方法
            thread_list.append(thread)

        # 让主线程等到所有的子线程结束，主线程再继续执行
        for thread in thread_list:
            thread.join()
        """
        # multiprocessing.dummy
        # 创建线程池对象
        pool = Pool(len(self.url_list))
        # 依次执行url_list里的每个url地址请求
        pool.map(self.send_request, self.url_list)
        # 关闭线程池
        pool.close()
        # 让主线程等待所有子线程结束，主线程再继续执行
        pool.join()

        # 判断队列是否为空
        while not self.data_queue.empty():
            # 打印队列中的信息
            print self.data_queue.get()


if __name__ == '__main__':
    start = time.time()
    spider = Douban()
    spider.start_work()
    print "[INFO]:Useing time:%f" % (time.time() - start)