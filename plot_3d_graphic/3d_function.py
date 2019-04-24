# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def first():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
    plt.show()


def draw_sphere(r):
    """
    alfa
    beta
    yama

    z = sin(alfa)*r
    x = cos(alfa)*sin(beta)*r
    y = cos(alfa)*cos(beta)*r
    :param r:
    :return:
    """

    angle = np.linspace(-2 * np.pi, 2 * np.pi, 50)
    x, y, z = 0, 0, 0
    matrix = np.array([[0, 0, 0]])
    for alfa in angle:
        for beta in angle:
            x = np.sin(alfa) * np.sin(beta) * r
            y = np.sin(alfa) * np.cos(beta) * r
            z = np.cos(alfa)*r
            new_row = np.array([[x, y, z]])
            matrix = np.vstack([matrix, new_row])

    # print(matrix[:,0])
    # print(matrix[:,1])
    # print(matrix[:,2])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(matrix[:, 0], matrix[:, 1], matrix[:, 2], 'gray')
    plt.fill(color="red")
    plt.show()

def draw_hiperbola(a,b,c):
    """
    alfa
    beta
    yama

    z = sin(alfa)*r
    x = cos(alfa)*sin(beta)*r
    y = cos(alfa)*cos(beta)*r
    :param r:
    :return:
    """

    angle = np.linspace(-2 * np.pi, 2 * np.pi, 50)
    x, y, z = 0, 0, 0
    matrix = np.array([[0, 0, 0]])
    for alfa in angle:
        for beta in angle:
            x = np.sin(alfa) * np.sin(beta) * a
            y = np.sin(alfa) * np.cos(beta) * b
            z = np.cos(alfa)*c/10
            new_row = np.array([[x, y, z]])
            matrix = np.vstack([matrix, new_row])

    # print(matrix[:,0])
    # print(matrix[:,1])
    # print(matrix[:,2])

    fig = plt.figure()
    plt.axis('equal')
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(matrix[:, 0], matrix[:, 1], matrix[:, 2], 'gray')
    z = [matrix[:, 0],matrix[:, 0]]
    print(z)
    ax.plot_surface(matrix[:, 0], matrix[:, 1],z, rstride=4, cstride=4, color='b')
    plt.fill(color="red")
    #Poly3DCollection

    plt.show()

def get_cordinate(x_func, y_funct, z_funct):
    pass


#draw_sphere(4)
draw_hiperbola(30,30,0.00000000000000000000000001)
#first()