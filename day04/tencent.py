# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json


class Tencent(object):
    def __init__(self):
        self.base_url = "http://hr.tencent.com/position.php?&start=0"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.page = 1
        self.item_list = []

    def send_request(self, full_url):
        try:
            html = requests.get(full_url, headers=self.headers).content
            return html
        except:
            print "[ERROR]:%s请求发送失败.." % full_url
            return None

    def parse_page(self, html):
        """解析职位列表页,并将每条职位信息保存到实例属性self.item_list"""
        soup = BeautifulSoup(html, 'lxml')
        # 当前页的所有职位结点列表
        node_list = soup.find_all('tr', {'class': ['odd', 'even']})
        # json
        for node in node_list:
            # 用来保存每个职位信息的字典
            item = {}
            # 职位名
            item["position_name"] = node.find('a').get_text()
            # 职位连接
            item["position_link"] = "http://hr.tencent.com/" + node.find("a").get("href")
            # 职位列表
            item["position_type"] = node.find_all("td")[1].get_text()
            # 招聘人数
            item["people_number"] = node.find_all("td")[2].get_text()
            # 工作地点
            item["work_location"] = node.find_all("td")[3].get_text()
            # 发布时间
            item["publish_times"] = node.find_all("td")[4].get_text()

            # 保存每条职位信息
            self.item_list.append(item)
        # 查找是否是最后一页
        # 如果是最后一页,函数返回True
        # 如果不是最后一页,则不做处理
        if soup.find("a", {"class": "noactive", "id": "next"}):
            return True

        # 提取下一页链接,并返回链接
        next_link = 'http://hr.tencent.com/' + soup.find("a", {"id": "next"}).get("href")
        return next_link

    def write_page(self):
        """写入数据"""
        # 将列表转为json字符串 再写入磁盘
        json.dump(self.item_list, open("tencent.json", "w"))

        # # 先将列表转成json字符串
        # json_str = json.dump(self.item_list)
        # with open('tencent.json','w') as f:
        #     # 将json字符串写入磁盘
        #     f.write(json_str)

    def start_work(self):
        # for page in range(0, 31, 10):
        #     full_url = self.base_url + str(page)
        #     html = self.send_request(full_url)
        #     if html:
        #         print '正在写入第%d' % (page / 10 + 1)
        #         self.parse_page(html)
        # self.write_page()
        html = self.send_request(self.base_url)
        while True:
            print '[INFO]:正在处理%d页面...' % self.page
            # 解析html响应,并接收self.parse_page()的返回值
            next_link = self.parse_page(html)
            # 如果next_link 为True 表示到了最后一页,则退出循环
            if next_link == True:
                break
            else:
                # 否则继续发送下一页链接请求,并接收返回html响应
                html = self.send_request(next_link)
                self.page += 1

        self.write_page()


if __name__ == '__main__':
    spider = Tencent()
    spider.start_work()
