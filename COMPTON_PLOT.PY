'''
PLOTTING THE ENERGY SHIFTS AS A FUNCTION OF ANGLE
TO VERIFY RELATIONSHIP OBEYS COMPTON RELATION
'''
import scipy as sp
import matplotlib.pyplot as plt

def energy(Bin):
    return -18.88445377853662 + Bin*2.7564950877963423

def Compton(theta,E):
    return E/(1+(E/500)*(1-sp.cos(theta)))

def plot(data_raw):
    data = sp.loadtxt(data_raw,skiprows=6,encoding='latin-1')

    source = []
    background = []
    source_minus = []
    
    for i in range(len(data)):
        source.append(data[i][1])
        background.append(data[i][2])
        source_minus.append(data[i][1]-data[i][2])
        

        
    energy_plot = sp.arange(0,len(background),1)
    
    plt.figure()
    plt.plot(energy_plot, source,label = 'source')
    plt.plot(energy_plot,source_minus,label = 'source without background')
    plt.xlabel('bins')
    plt.ylabel('count')
    plt.legend()
    plt.title(data_raw)
    plt.show()

peak_un=sp.array([241,241,216,201,187,164,140,132,116,108])
peak_uner=[7,8,16,8,8,24,24,10,19,4]


theta_data = (sp.linspace(0,90,10)*sp.pi)/180
energy_data = energy(peak_un)
theta = (sp.linspace(0,90,1000)*sp.pi)/180
plt.figure()
plt.plot(theta,Compton(theta,662),label = "Therotical Distrabution")
plt.scatter(theta_data,energy_data,label = 'data')
plt.xlabel("theta (rad)")
plt.ylabel("Energy (KeV)")
plt.legend()
plt.grid()

plot('CS40.txt')
