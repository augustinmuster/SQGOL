import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation as animation

#definitions of the possible states for the lattice
ALIVE=1
DEAD=0
states=[ALIVE,DEAD]

#lattice size
L = 6

# populate the grid with the "beacon" pattern
grid = np.array([[0,0,0,0,0,0],
        [0,1,1,0,0,0],
        [0,1,0,0,0,0],
        [0,0,0,0,1,0],
        [0,0,0,1,1,0],
        [0,0,0,0,0,0]])

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
    mat.set_data(newGrid)
    grid = newGrid
    return grid


# ################################################# FROM HERE SPECIFIC STUFF####################################################

#simulate the classical game of life from this random lattice
fig, ax = plt.subplots()
mat = ax.matshow(grid,cmap=cmap, norm=norm)
ani = animation.FuncAnimation(fig, update, interval=750, save_count=50)
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)
ani.save('beacon.mp4', writer=writer)
plt.show()
