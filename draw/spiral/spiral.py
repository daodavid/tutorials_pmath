import numpy as np
import matplotlib.pyplot as plt


print(np.sqrt(2))

def draw(args_X, args_Y):
    """
    :param args_X: args of x axes
    :param args_Y: args of y axes
    :return: null
    """
    plt.plot(args_X, args_Y)
    plt.show()





def get_codinates(call,r):
    result = [ np.exp(i/50)*call(i) for i in r]
    return result

r = np.linspace(-100,100,10000)
y = lambda y :np.sin(y)
x = lambda x :np.cos(x)


x_args = get_codinates(x,r)
y_args = get_codinates(y,r)


draw(x_args,y_args)
