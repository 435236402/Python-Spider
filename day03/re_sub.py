# -*- coding:utf-8 -*-

import re

p = re.compile(r"(\w+)\s(\w+)")

s = "python 123, hello 321,123 b"

result = p.sub(r"<\1> <\2>", s)
print result


# 会报错
# result = p.sub(r"<\1> <\2> <\3>", s)
# print result
