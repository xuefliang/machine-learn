# -*- coding: utf-8 -*-
"""
@author: xuefliang
@file: chapter08.py
@time: 6/26/16 4:46 PM
"""
import math
import matplotlib.pyplot as plt

x=[float(i)/100 for i in range(1,101,1)]
y=[i*math.log(i) for i in x]
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()