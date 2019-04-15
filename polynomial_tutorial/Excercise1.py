import math
import numpy as np
import matplotlib.pyplot as plt
import plotly as latex


class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        # for reasons of efficiency we save the coefficients in reverse order,
        # i.e. a_0, a_1, ... a_n
        self.coefficients = coefficients[::-1]  # tuple is also turned into list

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.

        """
        # The internal representation is in reverse order,
        # so we have to reverse the list
        return "Polynomial" + str(self.coefficients[::-1])

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x ** index
        return res


def interpolate_polynomial(arg):
    pass


def draw_function(my_funct, from_x, to_x):
    x_args = np.linspace(from_x, to_x, 1000)
    y_args = [my_funct(x) for x in x_args]
    plt.scatter(x_args, y_args)
    plt.show()


func = lambda x: x + 2

# draw_function(func, -10, 10)

p = Polynomial(2, 4, 5)
x = np.linspace(1, 100, 100)
y = p(x)
plt.plot(y, x)
plt.show()


def represent_polynomial(coeficinets):
    # p = Polynomial(coeficinets)
    # x = np.linspace(1, 100, 100)
    # y = p(x)
    # plt.plot(y, x)
    # plt.show()
    pass


represent_polynomial([1, 2, 4])


def test():
    ppar = [4, 3, -2, 10]
    p = np.poly1d(ppar)  # get instance polynom

    print(p(3))  # call instance as function
    print(np.polyval(ppar, 3))

    x = 3
    print(4 * x ** 3 + 3 * x ** 2 - 2 * x + 10)  #x alredy define python can ubderstand the


test()


def test_put_latex_expresion():
    a = r'\frac{a}{b}'
    ax = plt.axes([0, 0, 0.1, 0.2])  # left,bottom,width,height
    ax.set_xticks([])
    ax.set_yticks([])
    plt.text(0.3, 0.4, '$%s$' % a, size=40)  # put latex expresion in plot
    plt.show()





