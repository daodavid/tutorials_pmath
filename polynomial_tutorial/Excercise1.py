import math
import numpy as np
import matplotlib.pyplot as plot


def interpolate_polynomial(arg):
    pass


def draw_function(my_funct, from_x, to_x):
    x_args = np.linspace(from_x, to_x, 1000)
    y_args = [my_funct(x) for x in x_args]
    plot.scatter(x_args, y_args)


func = lambda x: x + 2

draw_function(func, 10, 10)
