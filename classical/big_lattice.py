
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
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


# ################################################# FROM HERE SPECIFIC STUFF####################################################

#simulate the classical game of life from this random lattice
fig, ax = plt.subplots()
mat = ax.matshow(grid,cmap=cmap, norm=norm)
ani = animation.FuncAnimation(fig, update, interval=300, save_count=200)
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)
ani.save('big_lattice.mp4', writer=writer)
plt.show()
