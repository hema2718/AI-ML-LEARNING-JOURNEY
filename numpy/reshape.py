import numpy as np

matrix = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print("Original Matrix")
print(matrix)

reshaped = matrix.reshape(2, 3)

print("Reshaped Matrix")
print(reshaped)