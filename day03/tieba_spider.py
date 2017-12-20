# -*- coding:utf-8 -*-

import re
import urllib2
import urllib
from lxml import etree

class TiebaSpider(object):
    def __init__(self):
        self.base_url = "http://tieba.baidu.com"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.tieba_name = raw_input("请输入你要爬取的贴吧名:")
        self.start_page = int(raw_input("请输入开始页:"))
        self.end_page = int(raw_input("请输入结束页"))

    def send_request(self,url):
        print '333'
        request = urllib2.Request(url, headers=self.headers)
        response = urllib2.urlopen(request)
        return response.read()

    def load_page(self, html):
        """处理帖子列表页,提取每个帖子的链接"""
        # 将 html 字符串转化成 HTML DOM对象
        print '11111'
        html_obj = etree.HTML(html)
        link_list = html_obj.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")
        return link_list

    def load_image(self, html):
        """处理每个帖子,提取里面的所有图片链接"""
        print '2222'
        html_obj = etree.HTML(html)
        link_list = html_obj.xpath("//img[@class='BDE_Image']/@src")
        return link_list

    def write_image(self,data,file_name):
        """将图片写入磁盘文件"""
        print "正在写入图片%s......" % file_name
        with open(file_name, 'wb') as f:
            f.write(data)

    def start_work(self):
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1)*50
            dict_obj = {"pn": pn, "kw": self.tieba_name}
            # 转码
            kw_str = urllib.urlencode(dict_obj)
            # 拼接正确的 url
            url = self.base_url + '/f?' + kw_str
            # 接收到返回的响应
            html = self.send_request(url)
            # 返回每个帖子的链接
            link_list = self.load_page(html)

            # 处理每个帖子的链接,提取图片的链接
            for link in link_list:
                # 拼接 每个帖子的 url
                full_url = self.base_url + link
                # 发送请求
                html = self.send_request(full_url)
                # 提取到图片链接
                image_link_list = self.load_image(html)

                # 处理每个图片的链接,发送请求并写入磁盘文件
                for link in image_link_list:
                    data = self.send_request(link)
                    self.write_image(data, link[-15:])


if __name__ == '__main__':

    spider = TiebaSpider()
    spider.start_work()
