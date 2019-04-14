from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

"""
begin starting pint 
end  ending point
points -number of points between start and end
"""
def write_comprehensive_array(start, end, num_point):
    points = []
    c = (end - start) / num_point
    for i in range(0, num_point):
        v=start + (c * i)
        points.append(v)
    return  points

def write(args_X=None, agrs_y=None):
    x = np.linspace(1, 4, 10)
    print(x)
    x = write_comprehensive_array(1,4,10)
    print(x)
    return x
"""
func = callable
array =array of args x
"""

def create_func(func,args):
    return [func(num) for num in args] #python single line loop created array using function to calculate values of new array using n comming from loop


array = write_comprehensive_array(1, 11, 1000)
print(array)
array2=create_func(lambda x: np.sin(x), array)
print(array2)


def plot_grapphic(x,y):

    ax = plt.gca()
    ax = plt.axes(projection='3d') #convert to 3d
    plt.plot(x, y)
    ax.scatter3D(x, y, x, x, cmap='Greens');  # write points
    ax.spines["left"].set_position("zero")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.show()

plot_grapphic(array,array2)


"""
write circle

"""