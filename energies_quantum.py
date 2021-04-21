import random
import math
import matplotlib.pyplot as plt

plotx=[]
# Number of points
N = 100000

# Inegration distance
box = 4.0
w=1
# Step Size
dx=float(box/N)

# Energy guess
E = float(input("Guess the energy: "))

def V(x):
    return 0.5*w*w*x*x
#def V(x):
#    if x<1:
#        return -5
#    elif x>=1:
#        return 0

def rhs(x,E,psi):
    return 2.0*(V(x)-E)*psi

#Define wave function and derivative
psi=[]
p=[]
xx=[]
# Initialize
for i in range(0,N):
    psi.append(0)
    p.append(0)
    xx.append(0)

# Boundary conditions
psi[0]=1.0
p[0]=0.0

# Leapfrog
for i in range(1,N):
    x = (i-1)*dx
    xx[i-1]=x

    psi[i]=psi[i-1]+(p[i-1]*dx)+(0.5*rhs(x,E,psi[i-1])*dx*dx)
    p[i]=p[i-1]+0.5*dx*(rhs(x,E,psi[i-1])+rhs(x+dx,E,psi[i]))

#normalize
sum=0.0
for i in range(0,N):
    sum+=psi[i]*psi[i]*dx

for i in range(0,N):
    psi[i]=psi[i]/math.sqrt(sum)

# Expectation value
expectation=0.0
for i in range(0,N):
    expectation+=xx[i]*xx[i]*psi[i]*psi[i]*dx

print(expectation)

psi2=[]
if psi[0] != 0:
    psi2=psi[::-1]
else:
    psi2=psi[::-1]
    psi2=[-x for x in psi2]

for i in range(-N,N):
    plotx.append(i*dx)

psi3=psi2+psi
plt.plot(plotx,psi3)
plt.title('Wavefunction Psi for E= %f' %E)
plt.ylabel('psi')
plt.grid(True)
plt.show()
