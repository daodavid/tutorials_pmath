import numpy as np
import matplotlib.pyplot as plt


def append_vector(x_start, y_start, x, y,color='blue'):
    plt.quiver(x_start, y_start, x, y, angles='xy', scale_units='xy', scale=0.01, color='blue')
    # plt.quiver([0], [0], [2 , angles='xy', scale_units='xy', scale=1)


def draw_vectot_field(x_funct, y_funct, range_X, range_Y, color='blue'):
    """
    r = x*x(e1) + y*x(e2)

    :param x_funt:
    :param y_funct:
    :param range_X:
    :param range_Y:
    :param color:
    :return:
    """
    plt.xlim(range_X[0], range_X[1])
    plt.ylim(range_Y[0], range_Y[0])
    plt.axis('equal')
    x_arg = np.linspace(range_X[0], range_X[1], 10)
    y_args = np.linspace(range_Y[0], range_Y[1], 10)

    for i in x_arg:
        for j in y_args:
            x = x_funct(i, j)
            y = y_funct(i, j)
            append_vector(i, j, x, y)

    plt.show()
# add = lambda x, y : x + y


f_x = lambda x,y : -x/(x**2 + y**2)
f_y = lambda x,y : -y/(x**2 + y**2)
draw_vectot_field(f_x,f_y,[-100,100],[-100,100])