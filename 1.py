#external module 
import numpy as np
#Create a numpy
array = np.array([1, 2, 3, 4, 5])
print(f"Original array: {array}")
# Perform element-wise operations
arr_plus_one = array + 1
print(f"Array after adding 1 to each element: {arr_plus_one}")

# Calculate the mean of the array
mean_value = np.mean(array)
print(f"Mean of the array: {mean_value}")

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nOriginal matrix:\n{matrix}")

# Get the shape of the matrix
matrix_shape = matrix.shape
print(f"Shape of the matrix: {matrix_shape}")

# Perform matrix multiplication (requires another matrix)
matrix_b = np.array([[7, 8], [9, 10], [11, 12]])
product = np.dot(matrix, matrix_b)
print(f"Matrix product:\n{product}")