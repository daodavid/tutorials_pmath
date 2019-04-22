import matplotlib.pyplot as plt
import numpy as np


class Vector_Base():
    def __init__(self, array):
        self.array = np.array(array)
        print(self.array[1, 0])

    def plotBasic(self):
        ax = plt.axes()
        ax.arrow(0, 0, self.array[0, 0], self.array[0, 1], head_width=0.3, head_length=0.2, fc='blue')
        ax.arrow(0, 0, self.array[1, 0], self.array[1, 1], head_width=0.3, head_length=0.2, fc='blue')
        # print(self.array[0:])

        # ax.arrow(self.array[0.0], self.array[1.0], head_width=0.3, head_length=0.2,
        #          fc='black', ec='black')  # create e1 axes
        # ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
        plt.xlim(-10, 10)  # show measure
        plt.ylim(-10, 10)

    def get_cordinate(self, vector):
        v = np.array([vector[0], vector[1]])
        # v = np.array([vector[0,0],vector[1,0]])
        result = self.array.dot(v)
        return result

    @classmethod
    def plot_vector(cls,vector,color='black'):
        print(vector)


vector_basic=Vector_Base([[1, 0],
                           [0, 1]])
vector_basic.plotBasic()
result = vector_basic.get_cordinate([1, 4])
Vector_Base.plot_vector(result)
vector_basic1=Vector_Base([[1,1],
                         [-1, 1]])
vector_basic1.plotBasic()
result = vector_basic.get_cordinate([1, 4])
Vector_Base.plot_vector(result)
print(result)
plt.show()
