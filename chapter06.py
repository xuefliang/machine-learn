# encoding: utf-8
"""
@author: xuefliang
@contact: xuefliang@gmail.com
@file: chapter06.py
@time: 2016-6-21 17:26
"""
from locale import normalize
from numpy import gradient

#w当前值，g当前梯度方向，a当前学习率，data数据
def calcAlpha(w, g, alpha, data):
	c1=0.3
	now=fw(w,data)
	wNext=assign(w)
	numberProduct(a,g,wNext)
	next=fw(wNext,data)
	#寻找足够大的a，使得h(a)>0
	count=30
	while next <now:
		a*=2
		wNext=assign(w)
		numberProduct(a,g,wNext)
		next=fw(wNext,data)
		count-=1
		if count ==0:
			break
	#寻找合适的学习率a
	count=50
	while next>now-c1*a*dotProduct(g,g):
		a/=2
		wNext=assign(w)
		numberProduct(a,g,wNext)
		next=fw(wNext,data)
		count-=1
		if count==0:
			break
	return a


def calcCoefficient(data,listA,listW,listLostFunction):
	N=len(data[0]) #维度
	w=[0 for in range(N)]
	wNew=[0 for i in range(N)]
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
		assign2(2,wNew) #更新权值
		times +=1

		listA.append(alpha)
		listW.append(assign(w))
		listLostFunction.append(fw(w,data))
	return w

"""
随机梯度下降SGD
"""
def calcAlphaStochast(w,g,data):
	c1=0.01
	now=fwStochastic(w,data)
	wNext=assign(w)
	numberProduct(a,g,wNext)
	next=fwStochastic(wNext,data)
	#寻找最大的a
	count=30
	while next<now:
		if a<1e-10:
			a=0.01
		else:
			a*=2
		wNext=assign(w)
		numberProduct(a,g,wNext)
		next=fwStochastic(wNext,data)
		count-=1
		if count==0:
			break
	#寻找合适的学习率a
	count=50
	while next>now-c1*a*dotProduct(g,g):
		a/=2
		wNext=assign(w)
		numberProduct(a,g,wNext)
		next=fwStochastic(wNext,data)

		count=1
		if count==0:
			break
	return a

def calccoefficient(data,lista,listw,listlesfunction):
	M=len(data)
	N=len(data[0])
	w=[0 for i in range(N)]
	wNew=[0 for in range(N)]
	g=[0 for i in range(N)]
	times=0
	alpha=100.0
	same=False
	while times<10000:
		i=0
		while i<M:
			j=0
			while j<N:
				g[j]=gradientStochastic(data[i],w,j)
				j+=1
			normalize(g)
			alpha=calcAlphaStochastic(w,g,alpha,data[i])
			numberProduct(alpha,g,wNew)

			print "times,i,alpha,fw,w,g:\t",times,i,alpha,fw(w,data),w,g
			if isSame(w,wNew):
				if times>5:
					same=True
					break
			assign2(w,wNew)

			lista.append(alpha)
			listW.append(assign(w))
			listtestfunction.appdend(fw(w,data))

			i+=1
		if same:
			break
		times+=1
	return  w

def calcCoefficient(data,listA,listW,listLosFunction):
	N=len(data[0])
	w=[0 for i in range(N)]
	wNew=[0 for i in range(N)]
	g=[0 for i in range(N)]

	times=0
	alpha=100.0
	while times <10000:
		j=0
		while j<N:
			g[j]=gradient(data,w,j)
			j+=1
		normalize(g)
		alpha=calcAlpha(w,g,alpha,data)
		numberProduct(alpha,g,wNew)

		print "tiems,alpha,fw,w,g\t",times,alpha,fw(w,data),w,g
		if isSame(w,wNew):
			break
		assign2(w,wNew)
		times+=1

		listA.append(alpha)
		listW.append(assign(w))
		listLostFunction.append(fw(w,data))
	return w