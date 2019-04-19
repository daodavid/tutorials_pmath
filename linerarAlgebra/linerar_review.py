import numpy as np

# matrixes

"""
every linear space contains an element E ,which have a following properties
if a belongs L
A*E=E*A=A
"""
E = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])  # kronicker matrix

print(E.shape)  # dimension of array

vector_x = np.array([[1], [2], [3]])

norma_x = np.sqrt(vector_x.T.dot(vector_x))  # scallar mutiplication
# print(norma_x)
x_tran = vector_x.T
vector_x = np.array([[1], [2], [3]])
# print(vector_x.shape)

A = np.array([[1, 2, 3], [0, 2, 3], [3, 2, 4]])
print(np.linalg.inv(A))  # inverse matrix
print(A.T)  # tranportaning A

c = E.dot(vector_x)

# eing values and eing vectors

A = np.array([[2, 0], [0, 9]])

print(np.sqrt(130))

eing_values = np.linalg.eig(A)  ##eing values
print(eing_values)
eing_vectors = np.linalg.eigh(A)
print(eing_vectors)
