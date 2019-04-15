import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as Polynomial


def interpolate(x_pints, y_points, deggree):
    """
    just test and explanation
    fittin polynom by using two array contain x and y
    x[i] = y[i] points that the polynomial must to satisfy
    this method is junst the wrapper of nympy.polyfit
    :return:  instance of polynom with type  ndarray contains coeficient of polynomials
    """
    return np.polyfit(x_pints, y_points, deggree)


def create_polynomial_function(coeficient, range):
    """
    creates polynomial accoding given coeficients
    :param coeficient: ndarray
    :param range: x belengs from range[0] to range[1]
    :return: double array x and y args
    """
    p = np.poly1d(coeficient)
    x_args = np.linspace(range[0], range[1], 20)
    y_args = [p(i) for i in x_args]
    return x_args, y_args  # return two args


def interpolate_test(x, y):
    x = np.array(x)
    y = np.array(y)
    poly = np.polyfit(x, y, 3)
    # print(poly)
    # print(np.poly1d(poly))
    # print(type(poly))
    p = np.poly1d(poly)
    x_args = np.linspace(1, 8, 20)
    y_args = [p(i) for i in x_args]
    plt.plot(x_args, y_args)
    plt.scatter(x, y, color='red')
    # plt.show()

    # print(p(1))
    # print(poly[1])
    # print(poly.__str__())


x = [1, 2, 3]
y = [2, 4, 6]
results = interpolate(x, y, 3)
args1, args2 = create_polynomial_function(results, [1, 10])
plt.plot(args1, args2)
plt.scatter(x, y, color='red')
plt.show()

interpolate_test([1, 2, 3], [2, 4, 6])
