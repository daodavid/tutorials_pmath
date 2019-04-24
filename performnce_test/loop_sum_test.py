import numpy as np
import time

"""
As programmers, we're used to writing for-loops to iterate over collections. 
This is quite OK but in Python makes the code slow (because it's an interpreted, dynamically-typed language)
. For example, a "standard" way of summing an array would be


However, there are better ways to do this. numpy works in C "behind the scenes". This means that:

Operations in C are very, very, VERY fast
Communication between C and Python is slow
This means we should prepare our code to use numpy arrays as much as possible.
First of all, this gives us a great computational advantage: the code is very fast. Second, it will look simpler and more beautiful. 
Compare the previous code with this one:
"""
array = [np.random.random() for i in range(1000000)]
print(len(array))

def sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum


start = time.time()

sum1 = sum(array)

print("Process time: " + str(time.time() - start))

start = time.time()
sum = np.sum(array)
assert int(sum)==int(sum1) , 'sums is different'
print("Process time np sum: " + str(time.time() - start))