import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#definitions of the basis states for the lattice
ALIVE=1
DEAD=0

# B,D,S operators
def birth():
    return ALIVE

def dead():
    return DEAD

def survive(state):
    return state

# G operators

def G(A,state):
    if(A>=0 and A<=1):
        return dead()
    elif(A>1 and A<=2):
        return (np.sqrt(2)+1)*(2-A)*dead()+(A-1)*survive(state)
    elif(A>2 and A<=3):
        return (np.sqrt(2)+1)*(3-A)*survive(state)+(A-2)*birth()
    elif(A>3 and A<=4):
        return (np.sqrt(2)+1)*(4-A)*birth()+(A-1)*dead()
    else:
        return dead()

#lattice size
L = 50
f=0.2

# populate grid with more filling f
size=(L,L)
grid=np.zeros(size)

for x in range(L):
    for y in range(L):
         rf=np.random.choice([1,0],1, p=[f,1-f])[0]
         if(rf==1):
             rl=np.random.random(1)[0]
             grid[x][y]=rl

print(grid)
#-------------------------some visualisation stuff and functions------------------------------

#define color map for the plot
cmap = mpl.colors.ListedColormap(['black','grey','white'])
bounds = [-1,0.0000001,0.99999999,1.5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)


#-------------------------other function for mean liveness------------------------------
def update_only_grid(grid):
    #print("update")
    newGrid = grid.copy()
    for i in range(L):
        for j in range(L):
            total = (grid[i, (j-1)%L] + grid[i, (j+1)%L] + grid[(i-1)%L, j] + grid[(i+1)%L, j] + grid[(i-1)%L, (j-1)%L] + grid[(i-1)%L, (j+1)%L] + grid[(i+1)%L, (j-1)%L] + grid[(i+1)%L, (j+1)%L])
            newGrid[i][j]=G(total,grid[i][j])
    grid = newGrid
    return grid


# ################################################# FROM HERE SPECIFIC STUFF####################################################
#lattice size
L = 100

# populate cells with various fillings
size=(L,L)

# grid1
grid1=np.zeros(size)
f1=0.1

for x in range(L):
    for y in range(L):
         rf=np.random.choice([1,0],1, p=[f1,1-f1])[0]
         if(rf==1):
             rl=np.random.random(1)[0]
             grid1[x][y]=rl

print(grid1)

# grid2
grid2=np.zeros(size)
f2=0.2

for x in range(L):
    for y in range(L):
         rf=np.random.choice([1,0],1, p=[f2,1-f2])[0]
         if(rf==1):
             rl=np.random.random(1)[0]
             grid2[x][y]=rl

print(grid2)

# grid3
grid3=np.zeros(size)
f3=0.3

for x in range(L):
    for y in range(L):
         rf=np.random.choice([1,0],1, p=[f3,1-f3])[0]
         if(rf==1):
             rl=np.random.random(1)[0]
             grid3[x][y]=rl

print(grid3)

totalgrid=[grid1,grid2,grid3]

#liveness variables
a1=[]
a2=[]
a3=[]

totala=[a1,a2,a3]

for i in range(300):
    for j in range(3):
        totala[j].append(totalgrid[j].mean())
        totalgrid[j]=update_only_grid(totalgrid[j])

for k in range(3):
    plt.plot(np.arange(0,300,1),totala[k],label=("grid "+str(k+1)))

plt.title("Mean Liveness <a>")
plt.xlabel("Generation")
plt.ylabel("Mean Liveness")
plt.legend()
plt.show()
