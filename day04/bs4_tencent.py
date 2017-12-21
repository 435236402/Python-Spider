# -*- coding:utf-8 -*-
import requests

url = "http://hr.tencent.com/position.php?&start=0"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

html = requests.get(url, headers=headers).content

print html.find("剑灵")  # 查找页面是否有你需要的数据 没有返回:-1