from builtins import ValueError

import numpy as np
import matplotlib.pyplot as plt


def plot_vector(vectors, color='b'):
    plt.quiver([0], [0], vectors[0], vectors[1], angles='xy', scale_units='xy', scale=1, color=color)
    # plt.quiver([0], [0], [2 , angles='xy', scale_units='xy', scale=1)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axis('equal')
    plt.show()


def plot_basis(vectors, color='blue', show=False):
    """
    every row response for one vector
    :param vectors: ndarray
    :return: none
    """
    plt.axis('equal')
    plt.xlim(-10, 10, 1)
    plt.ylim(-10, 10, 1)

    e1 = vectors[0, :]
    e2 = vectors[1, :]
    e3 = vectors[2, :]
    plt.quiver([0], [0], *vectors[0, :], angles='xy', scale_units='xy', scale=1, color=color)
    plt.quiver([0], [0], *vectors[1, :], angles='xy', scale_units='xy', scale=1, color=color)
    # plt.quiver([0], [0], *vectors[1, :], angles='xy', scale_units='xy', scale=1, color=color)
    if show:
        plt.show()


def get_liner_combination(v, basis):
    inv_matrix = np.linalg.inv(basis)
    # if np.array_equal(inv_matrix.dot(basis)):
    #   print(inv_matrix)
    # else:
    #   raise ValueError('The matrix can not to be basis')
    if np.linalg.det(basis) == 0:
        raise ValueError('The determinant is zero')

    result = v.dot(inv_matrix)
    return result


# plot_basis(np.array([[5, 0, 0], [0, 5, 0]]), color="red", show=True)

# plot_vector(v1)


main_bases = np.array([[1, 0],
                       [0, 1]])

second_bases = np.array([[1, 1],
                         [2, 1]])

v = np.array([1, 1])

v1 = get_liner_combination(v, main_bases)

# plot_vector(v1,color='blue')

print(1 * second_bases[0, :] + 1 * second_bases[1, :])

z = 3 * second_bases[0, :] + 2 * second_bases[1, :]  # cordinates in basic2 is [3,2]
# z is coridnata in main bases


print(z)
res = np.array(z).dot(np.linalg.inv(second_bases))  ## must to return cordinate in basis 2

assert np.array_equal(np.array([3, 2]), res), "the inverse does not work"

print(res)





# plot_vector(v2,color='red')


