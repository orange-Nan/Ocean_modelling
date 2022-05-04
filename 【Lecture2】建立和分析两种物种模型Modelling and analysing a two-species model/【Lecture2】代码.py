import numpy as np  
import matplotlib.pyplot as plt

#Model parameters
K      = 100.0        # 20   - Prey carrying capacity 
r      = 0.2          # 0.2  - Prey intrinsic growth rate

Cmax   = 1            # 1    - Maximal consumption rate of the predator
k_N    = 30           # 30   - Half saturation constant of Predator for Prey
e      = 0.2          # 0.2  - Predator assimilation coefficient
m      = 0.1          # 31   - Predator mortality rate

#Simulation settings
EndTime= 250          # The length of the simulation (arbitrary unit)
dt     = 0.5          # The time step of the simulation, determines accuracy
P = 10
N = 100

#Model definition
def get_dNdt(N,P):
    dNdt = r*(1-N/K)*N-Cmax*(N/(N+k_N))*P
    return dNdt

def get_dPdt(N,P):
    dPdt = e*Cmax*(N/(N+k_N))*P-m*P
    return dPdt

P_list = []
N_list = []
x_list = []

for i in range(0,int(EndTime/dt)):
    P_list.append(P)
    P = P+dt*get_dPdt(N,P)
    N_list.append(N)
    N = N+dt*get_dNdt(N,P)
    x_list.append(i)

fig = plt.figure(figsize=(6,6),dpi=200)
ax1 = fig.add_subplot(111)
line1 = ax1.plot(x_list,P_list,label='Predator',color = 'royalblue')
line2 = ax1.plot(x_list,N_list,label='Prey',color ='green')
a = plt.xlabel('Time')
b = plt.ylabel('Population size')
ax1.legend()

plt.savefig('C:/Users/LULU/Desktop/Lecture2.jpg')
plt.show()



