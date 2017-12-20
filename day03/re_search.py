import re

p = re.compile(r"\d+")
s = "abcd1234dcba4321"
m = p.search(s)
print m
print m.group()
m = p.search(s, 10)
print m.group()