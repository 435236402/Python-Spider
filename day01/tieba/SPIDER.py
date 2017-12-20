# -*- coding:utf-8 -*-

import urllib
import urllib2


def send_request(url,):
    headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    return response.read()


def write_html(name,html):
    with open(name, 'w') as f:
        f.write(html)


def main(tieba_name, begin_page, end_page):
    for page in range(begin_page, end_page + 1):

        # 拼接 url
        pn = (page - 1)*50
        base_url = "http://tieba.baidu.com/f?"
        keyword = {"kw":tieba_name, 'pn':pn}
        key_str = urllib.urlencode(keyword)
        url = base_url + key_str

        # 获取响应
        html = send_request(url)

        # 拼接名字
        name = tieba_name + str(page) + ".html"

        write_html(name, html)


if __name__ == '__main__':
    tieba_name = raw_input("请输入你要爬取的贴吧名字:")
    begin_page = int(raw_input("请输入爬取的起始页"))
    end_page = int(raw_input("请输入爬取的结束页"))
    main(tieba_name, begin_page, end_page)