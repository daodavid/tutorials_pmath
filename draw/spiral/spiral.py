import numpy as np
import matplotlib.pyplot as plt


print(np.sqrt(2))

def draw(args_X, args_Y):
    """
    :param args_X: args of x axes
    :param args_Y: args of y axes
    :return: null
    """
    ax = plt.axes()
    plt.plot(args_X, args_Y)
    plt.scatter(args_X,args_Y,color="black")
    ax.fill(args_X, args_Y, args_Y,args_X )
    plt.show()




"""
def get_codinates(call,r):
    result = [ np.exp(i/50)/100*call(i) for i in r]
    return result

r = np.linspace(-100,100,10000)
y = lambda y :np.sin(y)
x = lambda x :np.cos(x)


x_args = get_codinates(x,r)
y_args = get_codinates(y,r)


draw(x_args,y_args)
"""

def hiperbolic_spiral_cordinates(call,r):
    result = [1/i*call(i)*1000 for i in r]
    return result

def aritmetic_spiral_codinates(call, r):
    result = [(0.001 + 0.2*i)*call(i) for i in r]
    return  result

def logaritmetic_spira_coridnates(call , r):
    result = [np.exp(i*00.1)*call(i) for i in r ]
    return  result


r = np.linspace(0,500,1000)
y = lambda y :np.sin(y)
x = lambda x :np.cos(x)


x_args = hiperbolic_spiral_cordinates(x,r)
y_args = hiperbolic_spiral_cordinates(y,r)


draw(x_args, y_args)

x_args = logaritmetic_spira_coridnates(x,r)
y_args = logaritmetic_spira_coridnates(y,r)

draw(x_args, y_args)

x_args = aritmetic_spiral_codinates(x,r)
y_args = aritmetic_spiral_codinates(y,r)


draw(x_args,y_args)

draw( r ,[y(i) for i in r ])


theta = np.arange(0, 8*np.pi, 0.1)
a = 1
b = .2

for dt in np.arange(0, 2*np.pi, np.pi/2.0):

    x = a*np.cos(theta + dt)*np.exp(b*theta)
    y = a*np.sin(theta + dt)*np.exp(b*theta)

    dt = dt + np.pi/4.0

    x2 = a*np.cos(theta + dt)*np.exp(b*theta)
    y2 = a*np.sin(theta + dt)*np.exp(b*theta)

    xf = np.concatenate((x, x2[::-1]))
    yf = np.concatenate((y, y2[::-1]))

    p1 = plt.fill(xf, yf)

plt.show()