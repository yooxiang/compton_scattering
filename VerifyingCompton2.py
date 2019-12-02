# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:48:54 2019

@author: ahadj
"""

import scipy as sp
import matplotlib.pyplot as plt

Cs_137_30=sp.loadtxt('Cs137_CV_Pre_30d.txt',skiprows=6)
back_Cs_30=sp.loadtxt('Cs137_CV_Pre_30d_back.txt',skiprows=5)

CorrectedCs_30=[]
for i in range (511):
    CorrectedCs_30.append(Cs_137_30[i][1]-back_Cs_30[i][1])
    
plt.plot(sp.arange(0,len(back_Cs_30)-1,1),CorrectedCs_30)
#plt.plot(sp.arange(0,len(back_Cs_30)-1,1),Cs_137_30)  