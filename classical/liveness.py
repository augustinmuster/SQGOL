import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

#definitions of the possible states for the lattice
ALIVE=1
DEAD=0
states=[ALIVE,DEAD]

#lattice size
L = 50

# populate grid with more DEAD cells than ALIVE cells, but randomly
grid = np.random.choice(states, L*L, p=[0.1,0.9]).reshape(L, L)

#-------------------------some visualisation stuff and functions------------------------------

#define color map for the plot
cmap = mpl.colors.ListedColormap(['black','white'])
bounds = [-1,0.5,1.5]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

def update(data):
    #print("update")
    global grid
    newGrid = grid.copy()
    for i in range(L):
        for j in range(L):
            total = (grid[i, (j-1)%L] + grid[i, (j+1)%L] + grid[(i-1)%L, j] + grid[(i+1)%L, j] + grid[(i-1)%L, (j-1)%L] + grid[(i-1)%L, (j+1)%L] + grid[(i+1)%L, (j-1)%L] + grid[(i+1)%L, (j+1)%L])
            if grid[i, j]  == ALIVE:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = DEAD
            else:
                if total == 3:
                    newGrid[i, j] = ALIVE
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]

#-------------------------other function for mean liveness------------------------------
def update_only_grid(grid):
    #print("update")
    newGrid = grid.copy()
    for i in range(L):
        for j in range(L):
            total = (grid[i, (j-1)%L] + grid[i, (j+1)%L] + grid[(i-1)%L, j] + grid[(i+1)%L, j] + grid[(i-1)%L, (j-1)%L] + grid[(i-1)%L, (j+1)%L] + grid[(i+1)%L, (j-1)%L] + grid[(i+1)%L, (j+1)%L])
            if grid[i, j]  == ALIVE:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = DEAD
            else:
                if total == 3:
                    newGrid[i, j] = ALIVE
    grid = newGrid
    return grid


# ################################################# FROM HERE SPECIFIC STUFF####################################################
#lattice size
L = 100

# populate grid with more DEAD cells than ALIVE cells, but randomly
grid1 = np.random.choice(states, L*L, p=[0.3,0.7]).reshape(L, L)
grid2 = np.random.choice(states, L*L, p=[0.2,0.8]).reshape(L, L)
grid3 = np.random.choice(states, L*L, p=[0.1,0.9]).reshape(L, L)

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
