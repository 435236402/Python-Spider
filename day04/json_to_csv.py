# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import json
import csv

def json_to_csv():
    # json文件对象,权限是读
    json_file = file("lagou.json", "r")
    # csv文件对象,权限是写
    csv_file = file("lagou.csv", "w")

    # 读取json文件的数据,并返回python数据类型
    item_list = json.load(json_file)
    # 创建一个csv文件读写对象,参数是需要处理的csv文件
    csv_write = csv.writer(csv_file)

    # 获取第一个字典的所有的键,返回一维列表,作为csv文件的表头
    sheet = item_list[0].keys()

    # 获取所有数据部分,二维嵌套列表
    data = [item.values() for item in item_list]

    # 先写入表头部分,一行数据 参数是一个一维列表
    csv_write.writerow(sheet)
    # 再写入数据部分,多行数据,参数是一个二维的列表
    csv_write.writerows(data)

    csv_file.close()
    json_file.close()

if __name__ == '__main__':
    json_to_csv()


