import numpy as np  
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import math

#Model parameters
T1 = 60
L1 = 100
pi = 3.1415926

#Simulation settings
end_x = int(1000)
x_list = [i for i in range(1000)]
A_0 = 1

def wave(t,L2,T2):
    A_t = []
    for x in range(1000):
        A_t.append(A_0*(math.sin(2*pi*(x/L1-t/T1))+math.sin(2*pi*(x/L2-t/T2))))
    return A_t

fig,ax = plt.subplots(figsize=(8,4))

def draw_line(i):
    ax.clear()
    line = ax.plot(x_list,wave(i,90,50),color='b')
    plt.xlabel('Distance(m)',fontsize=12)
    plt.ylabel('Surface Elevation(m)',fontsize=12,y=0.5)
    plt.title('Wave 3 by Nephele',fontsize=16)
    return line

anim = FuncAnimation(fig=fig, func=draw_line, frames=np.arange(1,100), interval=200,repeat=False)

anim.save('C:/Users/LULU/Desktop/Wave3.gif', dpi=200, writer='imagemagick')



