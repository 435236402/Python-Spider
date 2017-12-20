# -*- coding:utf-8 -*-
import re

p = re.compile(r"\d+")
s = "abcd1234dcba4321"

m = p.match(s)
print m

# 从下标为3的开始匹配
m = p.match(s, 3)
print m

m = p.match(s, 4)

print m.group()
