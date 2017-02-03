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


def extraction_cor(x1, y1, x2, y2, x3, y3, x4, y4, cor):
    #if(çÇÇ≥Ç™ìØÇ∂Ç»ÇÁå¿äEílÇ…yÇê›íË/xç¿ïWÇ™ìØÇ∂Ç»ÇÁå¿äEílÇ…xÇê›íË)
    for i in xrange(1,int(max(corx)*2+1),1):#(min(corx), max(corx)*2, 1.0):
        if (((y4-y3)/(x4-x3))*(i*0.5 -x3)+y3) > cor[i,1] :                      #xà»è„
            print "A"
            # if (((y2-y1)/(x2-x1))(i*0.5-x1)+y1) < cor[i,1]:                  #xà»â∫
           #     for k in xrange(1,int(max(cory)*2+1,1 )):
           #         if ( ((x1-x2)/(y2-y1))(k*0.5 - y1)+x1) < cor[i,0] :       #yà»â∫
           #             if ( ((x3-x4)/(y4-y3))(k*0.5 - y3)+x3) > cor[i,0] :   #yà»è„
           #                 room[i, 0] = corx[i]
           #                 room[i, 1] = cory[i]
           #                 room[i, 2] =  SPL[i]

def reg_3(x1,x2,y1,y2,cor):
    hoge(x1,x2,cor)
    hoge2(y1,y2,rooma)

def hoge(x1,x2,cor):
    cnt = -1
    if (x1 == x2):
        for i in cor[:,0]:
            cnt = cnt +1
            if ( x1 <= i ): #óÃàÊÅ®Ç…Ç†ÇÈÇ∆Ç´
                print i
                rooma[cnt] = cor[cnt]
    return(rooma)
def hoge2(y1,y2,cor):
    cnt = -1
    if (y1 == y2):
        for k in cor[:,1]:
            cnt = cnt +1
            if ( y1 <= k ): #óÃàÊÅ´Ç…Ç†ÇÈÇ∆Ç´
                print i
                roomb[cnt] = cor[cnt]

def hoge3(x1,x2,y1,y2,cor):
    cnt = -1
    for i in cor[:,0]:
        cnt = cnt + 1
        if (((y2-y1)/(x2-x1))*(i -x1)+y1) <= cor[cnt,1]: #íºê¸ÇÊÇËëÂÇ´Ç¢íl
            rooma[cnt] = cor[cnt]
    return(rooma)



print "A"
#reg_3(3,3,8,8,cor)
#for i in xrange(200):
#    print i, roomb[i] , cor[i]

hoge3(1,8,1,8,cor)
for i in xrange(250):
    print rooma[i],cor[i]

#for x in rooma:
#    if x not in roomb:
#        room.append(x)
#print room

