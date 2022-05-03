import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

#Simulation settings
EndTime = 3600
dt = 1
z0_obj = -80
w0_obj = 0
pobj = 1025.5
p_0 = 1025
g = 9.8

#Model definition
def pamb(z):
    p = p_0-z*0.01
    return p

def get_w(w0,z0):
    w1 = w0 - dt*g*(pobj-pamb(z0))/pobj
    return w1

def get_z(w1,z0):
    z1 = z0 + dt*w1
    return(z1)

z_list = []
time_list = []
for time in range(0,EndTime,dt):
    w0_obj = get_w(w0_obj,z0_obj)
    z0_obj = get_z(w0_obj,z0_obj)
    z_list.append(z0_obj)
    time_list.append(time)

z_mean = np.mean(z_list)
       
fig = plt.figure(figsize=(6,4),dpi=200)
ax1 = fig.add_subplot(111)

#只画了单色的折线图，因为plt.plot只能统一设置线条颜色
line1 = ax1.plot(time_list,z_list,color='b')
line2 = ax1.axhline(y=z_mean,color='k',lw=2)

ax1.set_xlabel('time(seconds)',fontsize=12)
ax1.set_ylabel('z(m)',fontsize=12)
ax1.set_title('Oscillations of a Buoyant Object',fontsize=15)

plt.savefig('C:/Users/LULU/Desktop/Oscillations.jpg')
plt.show()