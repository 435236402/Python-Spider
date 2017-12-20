# -*- coding:utf-8 -*-

import re

p = re.compile(r"[\,\.\;\s\!\?]")
s = "ab. b... c,... !d?, e"
result = p.split(s)
print result
# 'ab','','b','','','','c','','','',''
a = "ab.1b.1.1.1c,.1.1.1!d?,1e"
v = p.split(a)
print v

# 字符串转成列表就用 split
# 列表转字符串调用 join() 方法  "".join(list)
