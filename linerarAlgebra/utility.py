import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1,1],[-2,2],[4,-7]])
origin = [0], [0] # origin point
print( V[:,0])
plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
plt.show()




def plot_vectors(vectors,clolors):
    origin = [0], [0]
