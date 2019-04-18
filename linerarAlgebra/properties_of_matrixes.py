import numpy as np

"""
A+B=B+A
(A+B)*y = y*A+y*B
"""
A = [[1, 3], [2, 4]]
K = [[1, 2], [2, 4]]
E = [[1, 0], [0, 1]]  # kronirec matrix
B = [[1, 1], [5, 2]]

A = np.array(A)
E = np.array(E)
B = np.array(B)



D = A.dot(B)
C = B.dot(A)

if ((D == A)[0][0]):
    print("Matrix mutiplacation is comutative")
else:
    print("Matrix mutiplacation is not comutative")

C = A.dot(E)
C = E.dot(A)

if ((A == C)[0][0] and (C == A)[0][0]):
    print("Exist single matrix wich every matrix multiply by it ,can change that matrix ")

D = (A + B) * 4
print(D)

C = B * 4 + A * 4

if ((D == C).all() and (D == C).all()):   #verry strance bug
    print("Matrix have distribute low in multiplacation by real numbers")
else:
    print("Matrix have not distribute low in multiplacation by real numbers")


Det =  np.linalg.det(A)

A_inv = np.linalg.inv(A)
print(A_inv)
C = A_inv.dot(A)
D = A.dot(A_inv)

if((C==D).all):
    print("Matrix mutiplacation betwenn one matrix and its inverse matrix is comutative")
print(C)

if((C==E).all()):
    print("Every matrix multiply be its inverse matrix give the single matrix")


latex = r'\begin{bmatrix} 1 & 2 & -1 \\ 3 & 0 & 1 \\ 0 & 2 & 4 \end{bmatrix}'
print(latex)


V1 = [1,3]
V1 = np.array(V1)
V2 = V1.dot(A)  # multiplacation by vector
print(V2)