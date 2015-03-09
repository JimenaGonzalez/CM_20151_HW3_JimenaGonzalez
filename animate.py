import numpy as np
import os
import pylab
import matplotlib as mp
from matplotlib import pyplot as plt
from matplotlib import animation

x=[]
y=[]

for archivo in os.listdir("./Test"):
    data= np.loadtxt(archivo)
    a= data[:0]
    b= data[:1]
    for i in range (len(a)):
        x.append(a[i])
        y.append(b[i])
    
fig = plt.figure()
def animate(i):
    d= x[i]
    f= y[i]
    line.set_data(d,f)
    return line

anim=animation.FunAnimation(fig,animate, init_func=int,frames=200,interval=20,blit=True)
   
plt.show()
