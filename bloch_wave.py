import random
import math
import matplotlib.pyplot as plt

plotx=[]
# Number of points
N = 10000
# Potential of the wells
H=10
# Initialize energy (stop searching for solutions at this energy)
maxE = H
E=0
# Define resolution of shooting method
RES = 0.000000001
#-------------------------------------------------------------------------------
# Functions

def V(x):
    if math.floor(x) % 2 == 0:
        return 0
    else:
        return H

def rhs(x,E,psi):
    return 2.0*(V(x)-E)*psi

def solve(E,N,dx):
    global psi
    psi=[]
    p=[]

    # Initialize psi,p
    for i in range(0,N):
        psi.append(0)
        p.append(0)

    # Boundary conditions
    psi[0]=0.0
    p[0]=1.0

    # Leapfrog
    for i in range(1,N):
        x=(i-1)*dx
        psi[i]=psi[i-1]+(p[i-1]*dx)+(0.5*rhs(x,E,psi[i-1])*dx*dx)
        p[i]=p[i-1]+0.5*dx*(rhs(x,E,psi[i-1])+rhs(x+dx,E,psi[i]))

    return psi[N-1]
#-------------------------------------------------------------------------------
# Loop through wells and shooting method
M = [600]
allowed_energies=[]
for m in M:
    print("Number of wells= ",m)
    energy=[]
    # Set up wells and free space:
    box=2*m
    # Wells are evenly spaced 'a' distance apart
    a = 1
    # step size
    dx=float(box/100000)

    # Shooting method: search for energies
    while E < 100:
        Elow = E # Lower energy bound
        Eup = E+0.01 # Upper energy bound

        psiup=solve(Eup,N,dx)
        psilow=solve(Elow,N,dx)
        prodwave=psiup*psilow

        # Immediately eliminate energy domains with no solutions
        # and move to next range
        if(prodwave>0):
          print("no allowed energy in the range", Elow,Eup)
          E+=0.01
          continue
        # Narrow down energy to desired resolution
        while(abs(Eup-Elow)>RES):
            # Bisection method
            E=(Eup+Elow)*0.5
            psimid=solve(E,N,dx)

            if psimid*psiup>0:
                Eup = E
                psiup = psimid
            else:
                Elow= E
                psilow=psimid

        if prodwave<0:
            print("There is an allowed energy at E=",E)
            energy.append(E)
            E+=0.01

    print("-------------------------------------------")
    allowed_energies.append(energy)
#-------------------------------------------------------------------------------
print(allowed_energies)

for i in energy:
    plt.axhline(y=i)
plt.title('Energy Banding 60 Well System (100 eV)')
plt.ylabel('Energy (eV)')
plt.axis([-1,1,0,500])
plt.show()
