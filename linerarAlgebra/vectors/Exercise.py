#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
#import skimage.io
# Write your imports here




def plot_vectors(vectors, colors):
    """
    Plots vectors on the xy-plane. The `vectors` parameter is a Python list.
    Each vector is specified in the format [start_x, start_y, end_x, end_y]

    plt.xlim(-100, 10)
    plt.ylim(-10, 10)
    plt.axis('equal')

    print(a1)
    print(a1[:,1])

    plt.quiver(x_start, y_start, 2,2, angles='xy', scale_units='xy', scale=1, color=colors)
    plt.show()

    """
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    a1 = np.array(vectors)
    x_start = a1[:, 0]
    y_start = a1[:, 1]
    x_end = a1[:, 2]
    y_end = a1[:, 3]
    print(x_end)
    plt.quiver(x_start, y_start, x_end , y_end , angles='xy', scale_units='xy', scale=1, color=colors)

    # plt.quiver([0], [0], [2 , angles='xy', scale_units='xy', scale=1)
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    #plt.show()


v = [3.5, 8.6]
e1, e2 = [[0, 5], [4, 0]]
a=[[0, 0, 1, 0], [0, 0, 0, 1]]
a = [[0, 0, i[0], i[1]] for i in [e1, e2, v]]
plot_vectors(a, ["red"]) # One vector
#plot_vectors([[0, 0, 1, 0], [0, 0, 0, 1]], ["red", "blue"]) # Two orthogonal vectors
#plot_vectors([[1, 1, -2, 3], [2, 1, -2.5, 1.5], [-3.2, -1.5, 0, 4.3]], ["red", "blue", "orange"]) # Three arbitrary vectors


v = np.array([[1,2,3,4]])


def get_inverse_matrix(e1, e2):
   # print(e1)
   # print(type(e1))
   # input_array = np.array(e1)
   # new_row = np.array(e2)
   #
   # new_array = np.vstack([input_array, new_row])
   # return np.linalg.inv(new_array)

   first_row = np.array(e1)
   new_row = np.array(e2)
   new_matrix = np.vstack([first_row, new_row])
   return np.linalg.inv(new_matrix)

def find_linear_combination_coefficients(e1, e2, v):
    """
    Returns the coordinates of the representation of v in the basis {e_1, e_2}.
    That is, the unknown coefficients in the linear combination v = lambda_1 * e_1 + lambda_2 * e_2
    """
    inv_bace  =  get_inverse_matrix(e1,e2)
    v = np.array(v)
    return v.dot(inv_bace)


e1, e2 = [[1, 0], [0, 1]]
v = [3.5, 8.6]

get_inverse_matrix(e1,e2)
# Find the unknown coefficients. Extract the logic in a function.
# It should accept the two basis vectors and the one we need to represent
# and should return the two coefficients
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
# Plot the three vectors
#plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

e1, e2 = [[0, 5], [4, 0]]
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
e1, e2 = [[0, 5], [4, 0]]
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
#plot_vectors([[0, 0, i[0], i[1] for i in [e1, e2, v]], "red", "blue", "green")

a = [[0, 0, i[0], i[1]] for i in [e1, e2, v]]
print(a)
plot_vectors(a,["red", "blue", "green"])
for i in [e1, e2, v]:
    print(i)