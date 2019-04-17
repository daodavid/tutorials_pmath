# import Crypto
import random
import numpy as np
from sympy.ntheory import factorint
import time


def inverse_factorint(facorint_arg):
    result = 1
    for x in facorint_arg:
        result = result * (x ** facorint_arg[x])
    return  result


random_integer = random.getrandbits(10)
print(random_integer)


start = time.time()
p = factorint(random_integer)
end = time.time()
print(end - start)
print("fact")

start = time.time()
inverse_result = inverse_factorint(p);
end = time.time()
start = time.time()
print(inverse_result)
print(end - start)
print("inve")


start = time.time()
"the code you want to test stays here"


def function_test_speed(random_integer):
    start = time.thread_time_ns()
    p = factorint(random_integer)
    end = time.thread_time_ns()
    print(end - start)
    start = time.thread_time_ns()
    inverse_result = inverse_factorint(p);
    end = time.thread_time_ns()
    print(end - start)


for i in range(100,110):
    random_integer = random.getrandbits(i)
    print("in number with bit "+str(random_integer))
    function_test_speed(random_integer)