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

fig = plt.figure(figsize=(10,20),dpi=200)
color_list = ['m','indigo','b','dodgerblue','c','g']

def draw_ax(i,L2,T2):
    ax=fig.add_subplot(6,1,i)
    line1 = ax.plot(x_list,wave(1,L2,T2),color=color_list[i-1])
    ax.set_xlabel('Distance(m)',fontsize=12)
    ax.set_ylabel('Surface Elevation(m)',fontsize=12,y=0.5)
    ax.set_title('Wave '+str(i)+'by Nephele',fontsize=16)
    return ax

draw_ax(1,100,50)
draw_ax(2,90,60)
draw_ax(3,90,50)
draw_ax(4,100,-60)
draw_ax(5,50,-30)
draw_ax(6,95,-30)

plt.subplots_adjust(wspace=0.25,hspace=0.5)
plt.savefig('C:/Users/LULU/Desktop/Wave.jpg')
plt.show()