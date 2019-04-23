import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
# import skimage.io
import math

print ("hello")


# def plot_vectors(vectors, colors, plt):
#     """
#     Plots vectors on the xy-plane. The `vectors` parameter is a Python list.
#     Each vector is specified in the format [start_x, start_y, end_x, end_y]
#     """
#     ax = plt.axes()
#
#     # ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
#     plt.xlim(-4, 4)  # show measure
#     plt.ylim(-4, 4)
#     print(colors)
#     m = np.array(vectors)
#     shape = m.shape
#     print(shape[1])
#     for i in range(shape[0]):
#         lenght_x = abs(m[i, 2] - m[i, 0])
#         lenght_y = abs(m[i, 3] - m[i, 1])
#         # print(math.abs(m[i,1]-m[i,2]))
#         #plt.quiver(m[i, 0], m[i, 1], m[i, 2], [i, 3], color=colors[i], angles='xy', scale_units='xy', scale=1)
#         ax.arrow(0, 0, 10, 0, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e1 axes
#         ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
#        # ax.arrow(m[i,0],m[i,1],m[i,2],m[i,3], head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e1 axes
#
#
# plot_vectors([[0, 0, 2, 3]], ["red"], plt)  # One vector
# plot_vectors([[0, 0, 1, 0], [0, 0, 0, 1]], ["red", "blue"], plt)  # Two orthogonal vectors
# plot_vectors([[1, 1, -2, 3], [2, 1, -2.5, 1.5], [-3.2, -1.5, 0, 4.3]],
#              ["red", "blue", "orange"],plt)  # Three arbitrary vectors
h1 = plt.quiver(1, 2, 4, 5)
h1.set('AutoScale','off')
#set(h1,'AutoScale','on', 'AutoScaleFactor', 2)
plt.show