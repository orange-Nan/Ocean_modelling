import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

#Model parameters
K = 0.0001
C_0 = 100

#Simulation settings
EndTime = 15
dt = 3600

#Model definition
def explicit_formula(C_0,K,EndTime,dt):
    C_n = []
    C_n.append(C_0)
    for i in range(1*dt,(EndTime+1)*dt,dt):
        C_0 = (1-dt*K)*C_0
        C_n.append(C_0)
    return C_n

def implicit_formula(C_0,K,EndTime,dt):
    C_n = []
    C_n.append(C_0)
    for i in range(1*dt,(EndTime+1)*dt,dt):
        C_0 = C_0/(1+dt*K)
        C_n.append(C_0)
    return C_n

def semi_implicit_formula(C_0,K,EndTime,dt):
    C_n = []
    C_n.append(C_0)
    for i in range(1*dt,(EndTime+1)*dt,dt):
        C_0 = ((1-0.5*K*dt)/(1+0.5*K*dt))*C_0
        C_n.append(C_0)
    return C_n
    
Time_list = [i for i in range(16)]
Time_label = []
Time_label.append('')
for i in range(6):
    Time_label.append(str(i*3)+':00') 
C_n1 = explicit_formula(C_0,K,EndTime,dt)
C_n2 = implicit_formula(C_0,K,EndTime,dt)
C_n3 = semi_implicit_formula(C_0,K,EndTime,dt)


fig = plt.figure(figsize=(6,6),dpi=200)
ax1 = fig.add_subplot(111)

line1 = ax1.plot(Time_list,C_n1,label='explicit_formula',color = 'royalblue')
line2 = ax1.plot(Time_list,C_n2,label='implicit_formula',color ='green')
line3 = ax1.plot(Time_list,C_n3,label='semi_implicit_formula',color='teal')

ax1.xaxis.set_major_locator(MultipleLocator(3))
ax1.set_xticklabels(Time_label)
ax1.set_xlabel('time(hour)',fontsize=12)
ax1.set_ylabel('concentration(%)',fontsize=12)
ax1.set_title('The Decay Problem',fontsize=15)
ax1.legend()

plt.savefig('C:/Users/LULU/Desktop/Decay.jpg')
plt.show()



