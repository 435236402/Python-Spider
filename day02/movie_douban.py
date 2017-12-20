# -*- coding:utf-8 -*-
"""
爬取豆瓣的喜剧电影排名
"""
import urllib2

url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20"
headers = {"Uesr-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

with open('douban.json','w') as f:
    f.write(response.read())