import numpy as np
import matplotlib.pyplot as plt

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
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle), np.cos(angle)]])
    return R


def get_translation_matrix(mutiplier):
    T = np.array([[mutiplier, 0],
                  [0, mutiplier]])
    return T


R = get_rotation_matrix(0)
"""
when determinant is equal 1 this means 
the matrix is orthogonal
"""
# print(R)
# print(np.linalg.det(R))  ## determinant is equal 1

# lets get the eigenvectors values  and vectors of R
# print(np.linalg.eig(R))

"""
rotation example
"""

x = np.array([[1],
              [0]])
origin = [0], [0]  # origin point

# plt.quiver(*origin, (x[:,0]), [0,1], color=['black','black'], scale=10)

ax = plt.axes()
ax.arrow(0, 0, 10, 0, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e1 axes
ax.arrow(0, 0, 0, 10, head_width=0.3, head_length=0.2, fc='black', ec='black')  # create e2 axes
plt.xlim(0, 10)  # show measure
plt.ylim(0, 10)

R = get_rotation_matrix(np.pi / 6)  # 30 degree
#  decoment to see result
#
# rot_x = R.dot(x)
#
# x = np.array([[1],
#               [0]])
#
# ax.arrow(2, 2, int(x[0, 0]), int(x[1, 0]), head_width=0.5, head_length=0.7, fc='red', ec='black')
#
# # plt.quiver(*origin, (x[:,0]),(u[:,0]),(u[:,0]), color=['black','black'], scale=10)
# # plt.quiver(*origin, x[:,0], color=['blue','black'], scale=10)
#
# u = R.dot(x)
#
# ax.arrow(2, 2, u[0, 0], u[1, 0], head_width=0.5, head_length=0.7, fc='lightblue', ec='black')
#
# u = R.dot(u)
#
# ax.arrow(2, 2, u[0, 0], u[1, 0], head_width=0.5, head_length=0.7, fc='green', ec='black')
#
# u = R.dot(u)
#
# ax.arrow(2, 2, u[0, 0], u[1, 0], head_width=0.5, head_length=0.7, fc='blue', ec='black')
#
plt.grid

# plt.show()


"""
let's see the tranlation of vector

the translation of vector
"""

x = np.array([[1],
              [2]])

#ax.arrow(2, 2, x[0, 0], x[1, 0], head_width=0.3, head_length=0.2, fc='blue', ec='black')

T = get_translation_matrix(3)

x = T.dot(x)
#ax.arrow(2, 2, x[0, 0], x[1, 0], head_width=0.3, head_length=0.2, fc='blue', ec='black')
#plt.show()     decoment to result

"""
the dot(scalar product is always the same number in every different coordinates system
"""



"""
lets to make some more to see the power of operators
if we want to roate some vector with 30 degree and to increase it with some mutiplier n
"""

R = get_rotation_matrix(np.pi/6)
T = get_translation_matrix(5)

x = np.array([[1],
              [1]])


ax.arrow(2, 2, x[0, 0], x[1, 0], head_width=0.3, head_length=0.2, fc='blue', ec='black')


transform = R.dot(T)
x = transform.dot(x)
ax.arrow(2, 2, x[0, 0], x[1, 0], head_width=0.3, head_length=0.2, fc='blue', ec='black' ,label='Arrow2')
plt.text(x[0, 0],x[1, 0], 'translation')
plt.show()