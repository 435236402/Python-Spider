# -*- coding:utf-8 -*-

import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import pymongo
import json


class Douyu(unittest.TestCase):
    # 构造方法（名字固定）
    def setUp(self):
        self.url = "http://www.douyu.com/directory/all"
        # 创建浏览器对象
        self.driver = webdriver.PhantomJS(executable_path="/Users/user/phantomjs-2.1.1-macosx/bin/phantomjs")
        # 保存所有主笔信息的列表
        self.info_list = []

        # 创建MongoDB数据库链接
        self.client = pymongo.MongoClient(host="172.16.160.130", port=27017)
        self.db = self.client["DouyuInfo"]
        self.collection = self.db["info"]

    # 具体的测试方法（test开头）
    def testDouyu(self):
        # 手动发的第一个请求，之后的请求通过点击下一页让浏览器发送即可
        self.driver.get(self.url)
        while True:
            # 循环获取每一页的响应页面html
            html = self.driver.page_source
            soup = BeautifulSoup(html, "lxml")
            # 当前页面里包含所有主播的结点
            node = soup.find("div", {"id": "live-list-content"})

            # 房间名
            room_list = node.find_all("h3", {"class": "ellipsis"})
            # 类型
            tag_list = node.find_all("span", {"class": "tag ellipsis"})
            # 主播名
            name_list = node.find_all("span", {"class": "dy-name ellipsis fl"})
            # 观众人数
            people_list = node.find_all("span", {"class": "dy-num fr"})

            # [(), (), ()]
            info_list = zip(room_list, tag_list, name_list, people_list)

            for room, tag, name, people in info_list:
                item = {}
                item["room"] = room.get_text().strip()
                item["tag"] = tag.get_text().strip()
                item["name"] = name.get_text().strip()
                item["people"] = people.get_text().strip()
                # self.collection.insert(item)
                print item['room'], item['tag'], item['name'], item['people']
                self.info_list.append(json.dumps(item))

            # == -1 表示没到最后一页，继续点击下一页
            # != -1 表示到了最后一页，退出点击
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break
            # 模拟下一页点击
            try:
                self.driver.find_element_by_class_name('shark-pager-next').click()
            except:
                pass

        # 通过set去重，set只能存储可hash数据，在转回列表
        item_list = list(set(self.info_list))
        for item in item_list:
            # 将json字符串转为python数据类型，并写入MongoDB数据库
            info = json.loads(item)
            self.collection.insert(info)

    # 析构方法（名字固定）
    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()
        print "执行结束"

if __name__ == '__main__':
    unittest.main()