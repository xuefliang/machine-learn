# -*- coding: utf-8 -*-
"""
@author: xuefliang
@file: chapter07.py
@time: 6/23/16 10:42 PM
"""
import numpy

x=1.5
d=0
a=0.01
for i in range(0,1000,1):
    d=numpy.gradient(x)
    x-=d*a

print a,x