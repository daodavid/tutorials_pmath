import numpy as np
import matplotlib.pyplot as plt


def get_projection_array(x, y):
    x = np.linspace(0, x, 10)
    y = [y for i in range(10)]
    return [x, y]


def scalar_mutiplication(x, y):
    return x.T.dot(y)


def get_cordinate(v, basic, tp="array"):
    x_component = scalar_mutiplication(v, basic[:, 0])
    y_component = scalar_mutiplication(v, basic[:, 1])
    if tp == "array":
        return np.array([[x_component],
                         [y_component]])
    else:
        return x_component[0], y_component[0]


def append_vector_plot(x, y, plt):
    z = get_projection_array(x, y)
    line1, = ax.plot(z[0], z[1], label='Using set_dashes()', color='green')
    line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    z = get_projection_array(y, x)
    line2, = ax.plot(z[1], z[0], label='Using set_dashes()', color='green')
    line2.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break

    ax.arrow(0, 0, x, y, head_width=0.3, head_length=0.2, fc='black', ec='black')


basis = np.array([[1, 0],
                  [0, 1]])

v1 = np.array([[1],
               [1]])
# dashes=[30, 5, 10, 5]

x, y = get_cordinate(v1, basis, "cm")
ax = plt.axes()
ax.arrow(0, 0, 10, 0, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e1 axes
ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
plt.xlim(0, 10)  # show measure
plt.ylim(0, 10)
append_vector_plot(x,y,plt)

plt.show()

"""
let to create other basic

"""
