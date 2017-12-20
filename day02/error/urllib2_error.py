# -*- coding:utf-8 -*-


import urllib2


def send_request():
    requset = urllib2.Request("http://www.sfdsfdsafsdfs.com")

    try:
        response = urllib2.urlopen(requset)
    except urllib2.URLError, e:
        print e
    print "hello world"


if __name__ == '__main__':
    send_request()