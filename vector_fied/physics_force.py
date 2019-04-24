import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D


def plot_vector_field(soav,scale=1):
    print(soav)
    X, Y, Z, U, V, W = zip(*soav)
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax = fig.gca( projection='3d')
    ax.quiver(X, Y, Z, U, V, W,color = 'red')
    ax.view_init(elev=18, azim=30)  # camera elevation and angle
    ax.dist = 8
    #ax.set_xlim([-10, 10])
    #ax.set_ylim([-10, 10])
    #ax.set_zlim([-10, 10])
    plt.show()


# plot_vector_field(1)


def create_vectors_matrix(x_call=None, y_call=None, z_call=None, range=[[-10, 10], [-10, 10], [-10, 10]] ,scale = 0.1,center_force=[0,0,0]):
    x_args = np.linspace(range[0][0], range[0][1], 7)
    y_args = np.linspace(range[1][0], range[1][1], 7)
    y_args = np.linspace(range[2][0], range[2][1],7)
    x_c = center_force[0]
    y_c = center_force[1]
    z_c = center_force[2]
    matrix = [0, 0, 0, 0, 0, 0]
    for x in x_args:
        for y in x_args:
            for z in x_args:
                if x==x_c or y==y_c or z==z_c:
                    continue
                new_row = np.array([x, y, z, x_call(x,y,z,z_c)*scale, y_call(x,y,z,y_c)*scale, z_call(x,y,z,z_c)*scale])
                matrix = np.vstack([matrix, new_row])

    return matrix

"""
nuton vector field
"""
x_func = lambda x,y,z,c: (c-x)/(math.sqrt((c-x)**2 + (c-y)**2 + (c-z)**2))
y_func = lambda x,y,z,c: (c-y)/(math.sqrt((c-x)**2 + (c-y)**2 + (c-z)**2))
z_func = lambda x,y,z,c: (c-z)/(math.sqrt(x**2 + y**2 + z**2))

matrix = create_vectors_matrix(x_func, y_func, z_func,scale=1,center_force=[11,11,11])
plot_vector_field(matrix)
