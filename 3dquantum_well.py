import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# Define 3D box:
Lx = 4.0
Ly = 4.0
N = 30

a=1
b=1

# Integration distance
dx=Lx/N
dy=Ly/N

#Guess energy:
E = float(input("Guess the energy: "))

# Potentials

def V(x=1,y=1):
    return 0.5*x*x*y*y

def rhs(a,E,psi):
    return 2.0*(V(a)-E)*psi

# Define wave function
psi_x=[]
p_x=[]
psi_y=[]
p_y=[]

# Initialize
for i in range(0,N):
    psi_x.append(0)
    psi_y.append(0)
    p_x.append(0)
    p_y.append(0)

# Boundary Conditions
psi_x[0]=0.0
psi_y[0]=0.0
p_x[0]=1.0
p_y[0]=1.0

# Leapfrog
for i in range(1,N):
    x = (i-1)*dx
    y = (i-1)*dy

    psi_x[i]=psi_x[i-1]+(p_x[i-1]*dx)+(0.5*rhs(x,E,psi_x[i-1])*dx*dx)
    p_x[i]=p_x[i-1]+0.5*dx*(rhs(x,E,psi_x[i-1])+rhs(x+dx,E,psi_x[i]))

    psi_y[i]=psi_y[i-1]+(p_y[i-1]*dy)+(0.5*rhs(y,E,psi_y[i-1])*dy*dy)
    p_y[i]=p_y[i-1]+0.5*dy*(rhs(y,E,psi_y[i-1])+rhs(y+dy,E,psi_y[i]))

# Normalize
sumx=0.0
sumy=0.0

for i in range(0,N):
    sumx+=psi_x[i]*psi_x[i]*dx
    sumy+=psi_y[i]*psi_y[i]*dy

for i in range(0,N):
    psi_x[i]=psi_x[i]/sumx
    psi_y[i]=psi_y[i]/sumy

psi_tot=np.zeros((N,N))
for i in range(0,N-1):
    for j in range(0,N-1):
        psi_tot[i,j]=(psi_x[i]+psi_y[j])

plotx=[]
ploty=[]
for i in range(0,N):
    plotx.append(i*dx)
for i in range(0,N):
    ploty.append(i*dy)

X, Y = np.meshgrid(plotx, ploty)

Z = psi_tot

fig=plt.figure()
ax= Axes3D(fig)
ax.plot_surface(X,Y,Z,rstride=1, cstride=1, cmap=cm.viridis)

plt.show()
