# -*- coding:utf-8 -*-

import urllib2
import urllib


def write_html(html, name):
    with open(name, 'w') as f:
        f.write(html)


def send_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()


def main(tieba_name, begin_page, end_page):
    for page in range(begin_page, end_page + 1):
        pn = (page - 1) * 50

        # 组织 url
        base_url = "https://tieba.baidu.com/f?"
        keyword = {"kw": tieba_name, "pn": pn}
        key_str = urllib.urlencode(keyword)
        url = base_url + key_str
        print url

        html = send_request(url)

        # 拼接抓取的名字
        name = tieba_name + str(page) + '.html'

        write_html(html, name)


if __name__ == '__main__':
    tieba_name = raw_input("请输入要抓取的贴吧名字")
    begin_page = int(raw_input("请输入要抓取的起始页"))
    end_page = int(raw_input("请输入要抓取的结束页"))

    main(tieba_name, begin_page, end_page)
