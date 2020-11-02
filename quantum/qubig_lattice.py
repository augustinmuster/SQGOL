
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

def update(data):
    #print("update")
    global grid
    newGrid = grid.copy()
    for i in range(L):
        for j in range(L):
            total = (grid[i, (j-1)%L] + grid[i, (j+1)%L] + grid[(i-1)%L, j] + grid[(i+1)%L, j] + grid[(i-1)%L, (j-1)%L] + grid[(i-1)%L, (j+1)%L] + grid[(i+1)%L, (j-1)%L] + grid[(i+1)%L, (j+1)%L])
            newGrid[i][j]=G(total,grid[i][j])
    mat.set_data(newGrid)
    grid = newGrid
    return [mat]



#simulate the classical game of life from this random lattice
fig, ax = plt.subplots()
mat = ax.matshow(grid,cmap=cmap, norm=norm)
ani = animation.FuncAnimation(fig, update, interval=300, save_count=200)
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)
ani.save('qubiglatt.mp4', writer=writer)
plt.show()
