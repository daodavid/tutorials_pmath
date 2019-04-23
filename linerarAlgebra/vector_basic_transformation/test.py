
import numpy as np
import matplotlib.pyplot as plt

def normvectorfield(xs, ys):
    """
    plot normalized vector field

    kwargs
    ======

    - length is a desired length of the lines (default: 1)
    - the rest of kwards are passed to plot
    """
   # length = kw.pop('length') if 'length' in kw else 1
    #x, y = np.meshgrid(xs, ys)
    # calculate vector field
    #vx, vy = fs(x, y)
    # plot vecor field
    #norm = length / np.sqrt(vx ** 2 + vy ** 2)
    plt.quiver(0, 0, xs * 10, ys * 10, angles='xy')
    V = np.array([[1, 1], [-2, 2], [4, -7]])
    origin = [0], [0]  # origin point
    print(V[:, 0])
    plt.quiver(*origin,1, 2, color=['r', 'b'], scale=21, angles='xy')
    plt.show()

    plt.show()



normvectorfield(2,2)