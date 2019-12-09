'''
PLOTTING THE ENERGY SHIFTS AS A FUNCTION OF ANGLE
TO VERIFY RELATIONSHIP OBEYS COMPTON RELATION
'''
import scipy as sp
import matplotlib.pyplot as plt

def energy(Bin):
    return fit_en[1] + Bin*fit_en[0]

def Compton(theta,E):
    return E/(1+(E/500)*(1-sp.cos(theta)))
              
theta = (sp.linspace(0,90,1000)*2*sp.pi)/180
plt.figure()
plt.plot(theta,Compton(theta,662),label = "Therotical Distrabution")
plt.xlabel("theta (rad)")
plt.ylabel("Energy (KeV)")
plt.legend()
plt.grid()