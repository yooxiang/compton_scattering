"""
Fourth session: calibrating the detector at 550V

"""

import scipy as sp
import matplotlib.pyplot as plt
import numpy as np


background=sp.loadtxt('back_550_29.txt',skiprows=5)
Cs_137=sp.loadtxt('Cs137_550V_29.txt',skiprows=6)
Am_241=sp.loadtxt('Am241_550_29.txt',skiprows=6)
Co_57=sp.loadtxt('Co57_550_29.txt',skiprows=6)

backgroundc=[]
for i in range(len(background)):
    backgroundc.append(background[i][1])

Cs_137c = []
for i in range(len(Cs_137)):
    Cs_137c.append(Cs_137[i][1])

x=sp.arange(0,len(backgroundc),1)
plt.figure()
plt.plot(x,backgroundc)
plt.figure()
#plt.plot(sp.arange(0,len(Cs_137c),1),Cs_137c)


CorrectedCs = []
CorrectedAm=[]
CorrectedCo=[]
for i in range (511):
    CorrectedCs.append(Cs_137[i][1] - background[i][1])
    CorrectedAm.append(Am_241[i][1] - background[i][1])
    CorrectedCo.append(Co_57[i][1] - background[i][1])
    
CorrectedAm = sp.array(CorrectedAm)

plt.plot(sp.arange(0,len(backgroundc)-1,1),CorrectedCs)
plt.plot(sp.arange(0,len(backgroundc)-1,1),CorrectedAm**0.6)
plt.plot(sp.arange(0,len(backgroundc)-1,1),CorrectedCo)
plt.legend(["Cs_137 Source with Background removed","Am_241 Source with Background removed","Co_57 Source with Background removed"])
plt.xlabel("Bins")
plt.ylabel("Counts")
plt.title("Calibrated histogram for all the sources 550 V (scaled)")
plt.xlim(0,300)
plt.savefig("550_fig", dpi = 1000)
#plt.savefig("22_11_Shisto_dpi", dpi = 1000)

