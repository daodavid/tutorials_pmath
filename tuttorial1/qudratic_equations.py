import math

def solve_quadratic_equation(a, b, c):  #a*x^2 + b^x + c
    if a==0:
        return [(-c/b)]
    d = (b**2)-4*a*c
    if d<0 :   #there is no real root
        return  []
    determinant = math.sqrt(d)
    x = (-b-determinant)/2*a
    y = (-b+determinant)/2*a
    if d==0 :  #only one root
        return [x]
    return [x,y]




