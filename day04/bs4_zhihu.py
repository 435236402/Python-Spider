# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

url = 'http://www.zhihu.com/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
html = requests.get(url, headers=headers).content
#  print html

soup = BeautifulSoup(html, 'lxml')

# print soup.find('input')  # 查找网页的第一个 input标签
# print soup.find('input').get('value')  # 第一个 input 标签的 value 属性值
# soup.find_all('input')  # 查找网页所有的 input 标签
# print soup.find('input', attrs={'name': '_xsrf'})  # 查找第一个name属性为_xsrf的input标签
#
# print soup.select("input[name='_xsrf']")  # 查找网页所有的name属性为_xsrf的input标签
# print soup.select("input[name='_xsrf']")[0].get('value')
# print soup.select("input[name='_xsrf']")[0].get_text()

from lxml import etree
html_obj = etree.HTML(html)
print html_obj.xpath("//input[@name='_xsrf']/@value")[0]