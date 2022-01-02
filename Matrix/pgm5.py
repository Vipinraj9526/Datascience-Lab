import numpy as np

a = np.array([[2, 4, 5], [5, 8, 1], [4, 2, 6]])
print("Matrix A:\n", a)
b = np.array([[1, 4, 2], [5, 2, 1], [4, 2, 3]])
print("Matrix B:\n", b)
print("Sum of Matrixs :\n", a + b)
print("Subtraction of Matrixs :\n", a - b)
print(np.dot(a,b))
