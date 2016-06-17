# -*- coding: utf-8 -*-
"""
@author: xuefliang
@file: chapter02.py
@time: 6/17/16 9:10 PM

从1,2,3,......,98,99,2015这100个数中任意选择若干个数(可能为0个数)求异或，试求异或的期望值。
"""
import random

a = range(1, 100)
a.append(2015)


def Sample():
    N = random.randint(0, 99)  # 在100个数中随机选取N个数
    t = random.sample(a, N)  # 返回a中的N个数
    t.sort(lambda a, b: a - b)  # 升序排序
    n = t[0]
    for i in range(len(t) - 1):
        n = n ^ t[i + 1]
        return n  # 异或值


print Sample()

sampleSize = 10000
s = 0
for i in range(sampleSize):
    s = sum([s, Sample()])

print s / sampleSize