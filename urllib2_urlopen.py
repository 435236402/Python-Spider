# -*- coding:utf-8 -*-

# 导入模块
import urllib2


def send_request():
    # urllib2.urlopen() 发送一个 url 地址的请求,并返回一个类文件的 response对象
    # 但是 urlopen 不能直接添加请求报头
    response = urllib2.urlopen("http://www.baidu.com/")

    # response 就是一个类文件对象,所以可以使用文件操作的相关方法.比如 read()
    # response.read()返回响应字符串,编码为网页的 charset编码
    print response.read()

if __name__ == '__main__':
    send_request()