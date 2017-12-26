# -*- coding:utf-8 -*-

import json

import pymongo


class Tencent(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __open(self):
        self.json_file = open('tencent.json', 'r')

        # 创建MongoDB数据库链接， 返回链接对象
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        # 指定数据库名称
        self.db = self.client["Mongo_Tencent"]
        # 指定集合名称
        self.collection = self.db["position"]

    def __close(self):
        self.json_file.close()

    def start_work(self):
        try:
            self.__open()

            list_obj = json.load(self.json_file)
            # 向集合里插入数据，如果是一个字典表示文档；如果是列表则表示多个文档
            self.collection.insert(list_obj)
            print "[INFO]数据存储成功..."
        except Exception, e:
            print "[ERROR]:数据存储失败..."
            print e
        finally:
            self.__close()

if __name__ == '__main__':
    tencent = Tencent('172.16.160.130', 27017)
    tencent.start_work()