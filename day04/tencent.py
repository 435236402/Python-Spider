# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Tencent(object):
    def __init__(self):
        self.base_url = "http://hr.tencent.com/position.php?&start="
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.page = 0

    def send_request(self, full_url):
        try:
            html = requests.get(full_url, headers=self.headers).content
            return html
        except:
            print "[ERROR]:%s请求发送失败.." % full_url
            return None

    def parse_page(self,html):
        soup = BeautifulSoup(html,'lxml')
        soup.find_all('tr')


    def start_work(self):
        for page in range(0, 2681, 10):
            full_url = self.base_url + str(page)
            html = self.send_request(full_url)
            if html:








if __name__ == '__main__':
    spider = Tencent()
    spider.start_work()