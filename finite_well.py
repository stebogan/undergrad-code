import random
import math
energy=[]
allowed_energies=[]
intercept=[]
add=-1
count=0
# Number of points
N = 100000
# Well size
a=1
H=5
# Inegration distance
box = 4.0

# Step Size
dx=float(box/N)

# Energy
energy=[-1,0]
value = True

def V(x):
    if x<a:
        return -H
    elif x>=a:
        return 0

def rhs(x,E,psi):
    return 2.0*(V(x)-E)*psi

def check(psi):
    global intercept
    if psi > 0:
        return intercept.append(1)

    else:
        return intercept.append(0)

# One version of shooting method
def shoot1(energy,E1,E2,dx,N):
    global E3
    E3 = (E1+E2)/2.0
    solve(N,E3,dx)

    if psi[N-1] < 0:
        energy[0]=E3
        return energy
    elif psi[N-1] > 0:
        energy[1]=E3
        return energy

# Second version of shooting method
def shoot2(energy,E1,E2,dx,N):
    global E3
    E3 = (E1+E2)/2.0
    solve(N,E3,dx)

    if psi[N-1] < 0:
        energy[1]=E3
        return energy
    elif psi[N-1] > 0:
        energy[0]=E3
        return energy

#Solve for psi
def solve(N,E,dx):
    global psi
    psi=[]
    p=[]

    # Initialize
    for i in range(0,N):
        psi.append(0)
        p.append(0)

    # Boundary conditions
    psi[0]=1.0
    p[0]=0.0

    for i in range(1,N):
        x=(i-1)*dx
        psi[i]=psi[i-1]+(p[i-1]*dx)+(0.5*rhs(x,E,psi[i-1])*dx*dx)
        p[i]=p[i-1]+0.5*dx*(rhs(x,E,psi[i-1])+rhs(x+dx,E,psi[i]))

    # Normalize
    sum=0.0
    for i in range(0,N):
        sum+=psi[i]*psi[i]*dx
    for i in range(0,N):
        psi[i]=psi[i]/sum

print("Computing...")

# Loop through energies until...
while(value):
    # Break if
    if energy[0]==-10:
        break
    intercept=[]

    for E in energy:
        solve(N,E,dx)
        check(psi[N-1])
    # If E2 + and E1 is -
    if intercept[1]-intercept[0] == 1 and count<20:
        if count == 19:
            allowed_energies.append(E3)
        shoot1(energy,energy[0],energy[1],dx,N)
        count+=1
        continue

    # If E2 - and E1 +
    elif intercept[1]-intercept[0] == -1 and count<20:
        if count == 15:
            allowed_energies.append(E3)
        shoot2(energy,energy[0],energy[1],dx,N)
        count+=1
        continue

    # If E1,E2 diverge in same direction
    else:
        if count == 1:
            allowed_energies.append(E3)

        energy=[add-1,add]
        add=add-1
        count=0
        continue

print("\n")
print("Allowed energies: ")
print(allowed_energies)
