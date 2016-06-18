# -*- coding: utf-8 -*-
"""
@author: xuefliang
@file: chapter03.py
@time: 6/18/16 8:24 AM
给定某正整数N，统计1到N！的所有数中，首位数字1出现的概率
"""
import matplotlib.pyplot as plt

def first_number(n):
    while n>=10:
        n=n/10
    return n

def second_number(n):
    while n>=100:
        n=n/10
    return n

if __name__=="__main__":
    n=1
    frequency=[0 for x in range(0,10,1)]
    for i in range(1,1000,1):
        n=n*i
        m=first_number(n)  #首位数字是几
        frequency[m]+=1  #首位数字1-9的统计
    print frequency
    frequency.remove(0)
    plt.plot(frequency,'r-',linewidth=2)
    plt.plot(frequency,'go',markersize=8)
    plt.show()