# -*- coding:utf-8 -*-

import requests
import urllib
import json
import jsonpath
import random
import time


class LagouSpider(object):
    def __init__(self):
        self.base_url = "http://www.lagou.com/jobs/positionAjax.json"
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "25",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "user_trace_token=20170923184359-1ba5fe6f-a04c-11e7-a60e-525400f775ce; LGUID=20170923184359-1ba6010d-a04c-11e7-a60e-525400f775ce; _ga=GA1.2.136733168.1506163440; JSESSIONID=ABAAABAAAGGABCB59B962955D91777BC94F49CBA0EAD056; _gid=GA1.2.1000657960.1513740225; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513740226; LGSID=20171220112341-2d420735-e535-11e7-9dd9-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; _gat=1; LGRID=20171220115524-9b85e27b-e539-11e7-9ddc-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513742130; SEARCH_ID=b5e518272f5c4585ab3bf889f6ca917d",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            # 反爬点1：检查请求的referer值，而且必须是合理的Referer值
            "Referer": "https://www.lagou.com/jobs/list_python?px=default&gx=&isSchoolJob=1&city=%E5%8C%97%E4%BA%AC",
            # "Referer" : "https://www.lagou.com/",
            # 反爬点2： 检查User-Agent
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest"
        }
        self.proxy_list = [{"http": "mr_mao_hacker:sffqry9r@120.27.218.32:16816"}, {}]
        self.position_name = raw_input("请输入需要抓取的职位:")
        self.city_name = raw_input("请输入需要抓取是城市:")
        self.page_num = int(raw_input("请输入需要抓取的页数"))
        self.page = 1
        self.item_list = []

    def send_request(self):
        formdata = {
            'first': 'true',
            'pn': self.page,
            'kd': self.position_name
        }

        params_data = {
            'px': 'default',
            'city': self.city_name,
            "needAddtionalResult": "false",
            "isSchoolJob": "1"
        }
        kw_str = urllib.urlencode(formdata)
        self.headers["Content-Length"] = str(len(kw_str))
        try:
            print '[INFO]:正在抓取数据....'
            response = requests.post(self.base_url, params=params_data, data=formdata, headers=self.headers, proxies=random.choice(self.proxy_list))
            return response
        except:
            print "[ERROR]:数据抓取失败"
            return None

    def parse_page(self, response):
        try:
            dict_obj = response.json()
            result_list = jsonpath.jsonpath(dict_obj, "$..result")[0]
            # print result_list
            for result in result_list:
                item = {}
                item["companyFullName"] = result["companyFullName"]
                item["positionName"] = result["positionName"]
                item["createTime"] = result["createTime"]
                item["city"] = result["city"]
                item["district"] = result["district"]
                item["salary"] = result["salary"]
                self.item_list.append(item)
        except:
            print "[ERROR]:数据解析失败..."

    def write_page(self):
        print "[INFO]:正在写入磁盘文件.."
        json.dump(self.item_list, open('lagou.json', 'w'))

    def start_work(self):
        while self.page <= self.page_num:
            response = self.send_request()
            if response:
                self.parse_page(response)
            time.sleep(2)
            self.page += 1

        self.write_page()

if __name__ == '__main__':
    spider = LagouSpider()
    spider.start_work()