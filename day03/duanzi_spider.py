# -*- coding:utf-8 -*-

import re
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class DuanziSpider(object):
    def __init__(self):
        self.base_url = "http://www.neihan8.com/article/index_"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 页码值
        self.page = 1

        # re.S表示启用 DOTALL模式,让.也可以匹配换行符
        self.pattern_page = re.compile(r'<div class="text-column-item box box-790">(.*?)</div>', re.S)
        # 匹配网页无用字符
        self.pattern_content = re.compile(r'<.*?>|&.*?;|\s|　')

    def send_request(self):
        # 第一页的地址为
        if self.page == 1:
            url = "http://www.neihan8.com/article/index.html"
        else:
            url = self.base_url + str(self.page) + '.html'
        print "正在发送第%d页请求" % self.page
        # 发送请求 返回网页原始编码字符串(utf-8)
        html = requests.get(url, headers=self.headers).content

        content_list = self.pattern_page.findall(html)
        return content_list

    def write_page(self, content_list):
        print "正在写入内容.."
        with open('duanzi.txt', 'a') as f:
            f.write("第%d页:\n" % self.page)
            for content in content_list:
                # 将每条内容的无用字符替换为空
                content = self.pattern_content.sub("", content)
                f.write(content)
                f.write('\n')
            f.write('\n')

    def start_work(self):
        while True:
            s = raw_input("请输入回车键开始爬取(退出请按Q):")
            if s == "Q":
                break
            content_list = self.send_request()
            self.write_page(content_list)
            self.page += 1
        print "成功退出"


if __name__ == '__main__':
    spider = DuanziSpider()
    spider.start_work()
