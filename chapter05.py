# -*- coding: utf-8 -*-
"""
@author: xuefliang
@file: chapter05.py
@time: 6/18/16 8:29 PM
"""

"""
给定定点和半径r，使得二维随机点等概率落在圆内
非均匀
"""
import math
import random
import matplotlib.pyplot as plt

x = [0 for x in range(0, 1000, 1)]
y = [0 for y in range(0, 1000, 1)]
for i in range(1, 1000, 1):
    r = random.randint(-50, 50)
    theta = random.uniform(0, 2 * math.pi)  # 弧度0-2*pi
    x[i] = r * math.cos(theta)
    y[i] = r * math.sin(theta)

plt.scatter(x[:1000], y[:1000])
plt.show()

"""
均匀
"""

x = [0 for x in range(0, 1000, 1)]
y = [0 for y in range(0, 1000, 1)]

m = [0 for m in range(0, 1000, 1)]
n = [0 for n in range(0, 1000, 1)]

for i in range(1, 1000, 1):
    x[i] = random.uniform(-50, 50)
    y[i] = random.uniform(-50, 50)
    if ((x[i] ** 2 + y[i] ** 2) < 2500):
        m[i] = x[i]
        n[i] = y[i]

plt.scatter(m[:1000], n[:1000])
plt.show()