import numpy as np

# 1. Array creation & reshaping
arr = np.arange(1, 10)
matrix = arr.reshape(3, 3)
print("3x3 Matrix:\n", matrix)

# 2. Basic mathematical operations
print("Matrix Squared:\n", matrix**2)
print("Column-wise Sum:", np.sum(matrix, axis=0))

# 3. Boolean indexing (filtering elements > 5)
filtered = matrix[matrix > 5]
print("Elements > 5:", filtered)