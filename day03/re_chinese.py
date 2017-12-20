# -*- coding:utf-8 -*-

import re

s = u"hello world,你好世界"

p = re.compile(ur"[\u4e00-\u9fa5]+")
result = p.findall(s)
print result[0]
print result
for i in result:
    print i