import math
import matplotlib.pyplot as plt
import numpy as np


def plot_math_function(f, min_x, max_x, num_points):
   x = np.linspace(min_x, max_x, num_points)
   f_vectorized = np.vectorize(f)
   y = f_vectorized(x)
   plt.plot(x, y)
   ax = plt.gca()
   ax.spines["left"].set_position("zero")
   ax.spines["top"].set_visible(False)
   ax.spines["right"].set_visible(False)
   #plt.show()
   plt.savefig('foo.png')


def plot_math_function(f, min_x, max_x, num_points):
   x = np.linspace(min_x, max_x, num_points)
   f_vectorized = np.vectorize(f)
   y = f_vectorized(x)
   plt.plot(x, y)
   ax = plt.gca()
   ax.spines["left"].set_position("zero")
   ax.spines["top"].set_visible(False)
   ax.spines["right"].set_visible(False)
   plt.show()


def plot_math_functions(functions, min_x, max_x, num_points):
   x = np.linspace(min_x, max_x, num_points)
   vectorized_fs = [np.vectorize(f) for f in functions]
   ys = [vectorized_f(x) for vectorized_f in vectorized_fs]
   for i in range(len(ys)):
      plt.plot(x, ys[i], 'C'+i.__str__())

   ax = plt.gca()
   ax.spines["left"].set_position("zero")
   ax.spines["top"].set_visible(False)
   ax.spines["right"].set_visible(False)
   plt.show()


plot_math_functions([lambda x: 2 * x + 3, lambda x: x], -3, 5, 1000)
plot_math_functions([lambda x: 3 * x**2 - 2 * x + 5, lambda x: 3 * x + 7], -2, 3, 1000)