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
print files


corx,cory, SPL = np.genfromtxt("SPL.txt", delimiter = ",", unpack =True)
print corx, cory, SPL

k = lambda
#liner1 = 

#for x in files:
#    no,ext = os.path.splitext(x)
#    name.append( int( str( no ) ) )#[name]へ取得したファイル名リスト[no]から取得して格納していく



#for x in xrange( len(name) ):
#    name[x] = str(name[x]) + '.csv'
#
#for file in xrange(len(name)):
#    filename = name[file]
#    x,y = np.genfromtxt(filename, delimiter = ",", unpack = True)
#    cor_x.append( x[0] *0.5 )
#    cor_y.append( y[0] *0.5 )
#
#print cor_x, cor_y
#for file in xrange(len(name)):
#    filename = name[file]
#    xlist,ylist = np.genfromtxt(filename,delimiter = ",", skip_header = 1,unpack = True )#, skip_header = 1  Tru
#    cal_SPL(xlist, ylist)



