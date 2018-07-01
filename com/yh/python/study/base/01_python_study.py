# 打印
import keyword
import random

r = random.random()
print(r)

print(keyword.kwlist)
agee = 18
if agee < 0 or agee > 120:
    print("error")
elif agee == 18:
    print("right")
"""
aaa
"""
print("yanhuan")
a = 2
b = "yanhuan" * 10
print(b)

price = 8.5
weight = 7.5
money = price * weight
if money > 50:
    print("超过50")
else:
    print("不超过50")
print(money - 5)

flag = False
print(flag)
print(type(flag))
"""
qingshuru = input("qingshuru")
print(qingshuru)
"""

name = "xiaoming"
print("欢迎%s" % name)

age = 18
print("年龄%06d" % age)
