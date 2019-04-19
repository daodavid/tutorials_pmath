import numpy as np

# what does it mean linear transformation

"""
def -->  A linear transformation T:U->V,is a
function or operator that carries elements of vector space U(called domain)
to vector space V(called cododomain),and which has to two aditional properties
T(u1) + T(u2) = T(u1) + T(u2) for all u1,u2∈U
T(αu)=αT(u)


(T+S)(u)=T(u)+S(u)
(αT)(u)=αT(u)
(S∘T)(u)=S(T(u)) composition
"""

#  let's consider the  matrices A and B  as linear operators that act over vector(linear) space L

A = np.array([[1, 3, 4],
              [2, 3, 4],
              [4, 3, 2]])

B = np.array([[2, 4, 5],
              [4, 5, 6],
              [4, 5, 3]])

# let's  get the vectors x and y belongs of vector space L

x = np.array([[1],
              [2],
              [4]])

y = np.array([[3],
              [5],
              [7]])

result1 = A.dot(x + y)
result2 = A.dot(x) + A.dot(y)
if (result1 == result2).all:
    print("distributed")

result1 = 5 * A.dot(x)
result2 = 5 * A.dot(x)

if (result1 == result2).all:
    print("commutative in multiplication by real numbers")

C = A.dot(B)
result1 = C.dot(x)
result2 = B * (A.dot(x))
if (result1 == result2).all:
    print("composition of operators is real fact")

# let's to review some advance theorем
"""
let's define rotation of vector 

Oiler matrix 

[sin(a) , 0 , 0]
[0  , cos(a) , 0]
[0 , 0 . cos(a)]

"""


def get_rotation_matrix(angle):
    R = np.array([[int(np.cos(angle)), -np.sin(angle)],
                  [np.sin(angle), int(np.cos(angle))]])
    return R

R = get_rotation_matrix(0)
"""
when determinant is equal 1 this means 
the matrix is orthogonal
"""
print(R)
print(np.linalg.det(R))  ## determinant is equal 1


# lets get the eing values of R

print(np.linalg.eig(R))

"""
the dot(scalar product is always the same number in every different coordinates system
"""
