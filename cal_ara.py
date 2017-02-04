#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *
import math
import matplotlib as mpl
import numpy as np
import glob, os


files = glob.glob('*.txt')
files.sort
name  = []
out = []

corx,cory, SPL = np.genfromtxt("SPL.txt", delimiter = ",", unpack =True)
point_x, point_y = np.genfromtxt("points.txt", delimiter = ",",unpack =True)

print corx, cory, SPL
cor  = np.zeros((len(SPL), 3))
rooma = np.zeros((len(SPL), 3))
roomb = np.zeros((len(SPL), 3))
room = np.zeros((len(SPL), 3))

pt  = np.vstack((point_x,point_y)).T
for i in xrange( len(corx) ):
    cor[i, 0] = corx[i]
    cor[i, 1] = cory[i]
    cor[i, 2] =  SPL[i]



def hoge(x1,x2,line,d):
    """
    x1,x2:座標
    cor  :全体座標データのリスト
    d    :左右のどちらを対象とするかd=1:右，d=2:左
    """
    cnt = -1
    if (x1 == x2):
        for i in cor[:,0]:
            cnt = cnt +1
            if (d == 1):
                if ( x1 <= i ): #|線|→にあるとき
                    print i
                    rooma[cnt] = line[cnt]
                else:
                    rooma[cnt] = 0
            elif(d== 2):
                if ( x1 >= i ): #←|線|にある場合
                    print i
                    rooma[cnt] = line[cnt]
                else:
                    rooma[cnt] = 0

def hoge2(y1,y2,line,d):
    """
    d:   上下どちらを対象とするかd=1:上,d=2:下
    """
    cnt = -1
    if (y1 == y2):
        for k in cor[:,1]:
            cnt = cnt +1
            if (d == 1):
                if ( y1 <= k ): #領域が↑にあるとき
                    print k
                    roomb[cnt] = line[cnt]
                else:
                    roomb[cnt] = 0
            elif(d==2):
                if ( y1 >= k ): #領域が↓にあるとき
                    print k
                    roomb[cnt] = line[cnt]
                else:
                    roomb[cnt] = 0

def hoge3(x1,x2,y1,y2,cor,d):
    cnt = -1
    for i in cor[:,0]:
        cnt = cnt + 1
        if (((y2-y1)/(x2-x1))*(i -x1)+y1) <= cor[cnt,1]: #直線より大きい値
            rooma[cnt] = cor[cnt]
        elif (((y2-y1)/(x2-x1))*(i -x1)+y1) >= cor[cnt,1]: #直線より小さい値
            rooma[cnt] = cor[cnt]
    return(rooma)

def cal_reg(x1,x2,y1,y2,cor,d1,d2):
    hoge (x1,x1,cor ,d1)
    hoge (x2,x2,rooma,d2)
    hoge2(y1,y1,rooma,d1)
    hoge2(y2,y2,roomb,d2)

def main():
    cal_reg(3,6,1,4,cor,1,2)

print "A"
main()


"""
for i in xrange(300):
    print roomb[i],cor[i]

A=SPL.reshape(19,19)
def draw(data,cb_min,cb_max):  #cb_min,cb_max:カラーバーの下端と上端の値
    import numpy as np
    import matplotlib.pyplot as plt
    X,Y=np.meshgrid(np.arange(data.shape[1]),np.arange(data.shape[0]))
    plt.figure(figsize=(10,4))  #図の縦横比を指定する
    div=20.0                    #図を描くのに何色用いるか
    delta=(cb_max-cb_min)/div
    interval=np.arange(cb_min,abs(cb_max)*2+delta,delta)[0:int(div)+1]
    plt.contourf(X,Y,data,interval)
    plt.show()
draw(A,0,100)
"""
