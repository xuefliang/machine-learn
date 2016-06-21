# encoding: utf-8
"""
@author: xuefliang
@contact: xuefliang@gmail.com
@file: chapter06.py
@time: 2016-6-21 17:26
"""
from locale import normalize

from numpy import gradient


def calcCoefficient(data,listA,listW,listLostFunction):
	N=len(data[0]) #维度
	W=[0 for in range(N)]
	WNew=[0 for i in range(N)]
	g=[0 for i in range(N)]

	times=0
	alpha=100.0 #学习率随意初始化
	while times<10000:
		j=0
		while j<N:
			g[j]=gradient(data,w,j)
			j+=1
		normalize(g) #正则化梯度
		alpha=calcAlpha(w,g,alpha,data)
		numberProduct(alpha,g,wNew)

		print "times,alpha,fw,w,g:\t",times,alpha,fw(w,data),w,g
		if isSame(w,wNew):
			break
		assign2(2,wNew)
		times +=1

		listA.append(alpha)
		listW.append(assign(w))
		listLostFunction.append(fw(w,data))
	return w