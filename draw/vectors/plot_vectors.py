import numpy as np
import matplotlib.pyplot as plt

V = np.array([[1,1],[-2,2],[4,-7]])
origin = [0], [0] # origin point
ax = plt.axes()
ax.spines["left"].set_position("zero")
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(False)

ax.arrow(0, 0, 0.5, 0.5, head_width=0.05, head_length=0.1, fc='k', ec='k')
plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
plt.show()