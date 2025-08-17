# Day 4 - NumPy Practice
# Author: Yorqinoy
# GitHub: https://github.com/yorqinoyyy
# Description: This file contains NumPy practice examples focused on array generation,
# basic operations, indexing, statistics, and matrix manipulations.

import numpy as np

# 1. Create an array of 10 zeros
zeros_array = np.zeros(10)
print("Array of zeros:", zeros_array)

# 2. Create an array of 10 ones
ones_array = np.ones(10)
print("Array of ones:", ones_array)

# 3. Create an array of 10 fives
fives_array = np.ones(10) * 5
print("Array of fives:", fives_array)

# 4. Create an array of integers from 10 to 50
range_array = np.arange(10, 51)
print("Array from 10 to 50:", range_array)

# 5. Create an array of even integers from 10 to 50
even_array = np.arange(10, 51, 2)
print("Even array from 10 to 50:", even_array)

# 6. Create a 3x3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 matrix:\n", matrix_3x3)

# 7. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity matrix:\n", identity_matrix)

# 8. Generate a random number between 0 and 1
random_number = np.random.rand()
print("Random number:", random_number)

# 9. Generate an array of 25 random numbers from a standard normal distribution
random_array = np.random.randn(25)
print("Random array:\n", random_array)

# 10. Create an array of 20 linearly spaced points between 0 and 1
linspace_array = np.linspace(0, 1, 20)
print("Linspace array:", linspace_array)


# ----------------- 🔷 Murakkab misollar -----------------

# 11. Select a submatrix from a given 5x5 matrix
base_matrix = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 matrix:\n", base_matrix)

# 12. Extracting a 3x3 submatrix
sub_matrix = base_matrix[2:, 1:]
print("Submatrix 3x3:\n", sub_matrix)

# 13. Fancy indexing and conditional selection
# Extract all values from base_matrix that are greater than 15
greater_15 = base_matrix[base_matrix > 15]
print("Values > 15:\n", greater_15)

# ----------------- 🔷 Professional level misollar -----------------

# 14. Normalize matrix rows to sum up to 1
matrix_for_norm = np.random.randint(1, 10, (4, 4))
print("Original matrix:\n", matrix_for_norm)

row_sums = matrix_for_norm.sum(axis=1).reshape(-1, 1)
normalized_matrix = matrix_for_norm / row_sums
print("Row-normalized matrix:\n", normalized_matrix)

# 15. Compute correlation coefficient between two random arrays
arr1 = np.random.randn(1000)
arr2 = np.random.randn(1000)

correlation = np.corrcoef(arr1, arr2)
print("Correlation coefficient between arr1 and arr2:\n", correlation)
