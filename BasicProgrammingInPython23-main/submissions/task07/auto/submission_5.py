#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 7
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: NumPy.
# 
# ___
# 
# **DEADLINE**:  19th June until 12:15  
# **Your name here**: Lale CAN  
# **Your university mail**: lcan@uos.de
# 
# ___
# 
# **Important information**:  
# In order to pass this sheet you need to achieve  /  points.  
# For the best possible grade you require  /  points, however, since some harder tasks may take a lot of time you don't have to pressure yourself.  
# If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
# Hand in your sheet in studip in the respective folder until the deadline.  
# If you receive no email until a few days after submission you will have passed, the sample solution will also be uploaded around then.  
# If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  

# ### Task 1 - Array Manipulation (4 points)
# 
# Create a Python program that takes a 1D NumPy array of size 10 with random integer values between 1 and 100 (inclusive) and performs the following operations:
# 
# - Create the 1D array with the specified size.
# - Reshape the array into a 2x5 matrix.
# - Transpose the matrix.
# - Finally, find the index of the maximum value in the array.

# In[1]:


import numpy as np

# Create a 1D NumPy array of size 10 with random integer values between 1 and 100
array = np.random.randint(1, 101, 10)
print("Original 1D array:")
print(array)

# Reshape the array into a 2x5 matrix
matrix = array.reshape(2, 5)
print("Reshaped 2x5 matrix:")
print(matrix)

# Transpose the matrix
transposed_matrix = matrix.T
print("Transposed matrix:")
print(transposed_matrix)

# Find the index of the maximum value in the array
max_index = np.argmax(array)
print("Index of maximum value:", max_index)


# ### Task 2 - Standart Deviation Ratio (SDR) (4 points)
# 
# Implement a Python program that calculates the standard deviation ratio (SDR) of a given 1D NumPy array. SDR represents the ratio of the standard deviation of the positive elements to the standard deviation of the negative elements.
# 
# - Create a 1D array of 100 random values.
# - Split the array into positive and negative elements.
# - Calculate the standard deviations of the positive and negative arrays.
# - Calculate the standard deviation ratio (SDR).

# In[2]:


import numpy as np

# Create a 1D array of 100 random values
array = np.random.randn(100)
print("Original array:")
print(array)

# Split the array into positive and negative elements
positive_array = array[array > 0]
negative_array = array[array < 0]

# Calculate the standard deviations of the positive and negative arrays
positive_std = np.std(positive_array)
negative_std = np.std(negative_array)

# Calculate the Standard Deviation Ratio (SDR)
sdr = positive_std / negative_std

print("Standard Deviation Ratio (SDR):", sdr)


# ### Task 3 - Identity Matrix (3 points)
# 
# Create a 5x5 identity matrix where:
# 
# - All diagonal elements are equal to 0.
# - The rest of the elements should be random integers between 0 and 50 (inclusive).

# In[3]:


import numpy as np

# Create a 5x5 identity matrix
matrix = np.eye(5)

# Generate random integers between 0 and 50 for non-diagonal elements
non_diag_values = np.random.randint(0, 51, size=(5, 5)) * (1 - np.eye(5))

# Add the non-diagonal values to the matrix
matrix += non_diag_values

print("Resulting 5x5 matrix:")
print(matrix)



# ### Task 4 - Calculate the Euclidean distance between two arrays (2 points)
# The Euclidean distance measures the straight-line distance between two points in space. In this task, you will calculate the Euclidean distance between two 1-dimensional arrays using the NumPy library.
# 
# **Hint:** To calculate the Euclidean distance between the two arrays, we can use the np.linalg.norm() function. This function calculates the norm, which is a generalized form of the Euclidean distance, of the difference between the arrays:
# 

# In[4]:


import numpy as np

# Two example 1-dimensional arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Calculate the Euclidean distance between the two arrays
euclidean_distance = np.linalg.norm(array1 - array2)

print("Euclidean distance:", euclidean_distance)


# ### Task 5 - Find the Point of Exceeding a Cumulative Sum Threshold (4 points)
# 
# Generate a random 1-dimensional array of size 100 with values ranging from 0 to 9. Calculate the cumulative sum of the array and find the index where the cumulative sum exceeds 100 for the first time, then print the index.
# Description:
# In this task, you will work with a randomly generated 1-dimensional array of numerical values. Your goal is to calculate the cumulative sum of the array, which represents the running total of the values. Then, you need to identify the position in the array where the cumulative sum exceeds a specific threshold.

# In[5]:


import numpy as np

# Generate a random 1-dimensional array of size 100 with values ranging from 0 to 9
array = np.random.randint(0, 10, size=100)
print("Original array:")
print(array)

# Calculate the cumulative sum of the array
cumulative_sum = np.cumsum(array)
print("Cumulative sum:")
print(cumulative_sum)

# Find the index where the cumulative sum exceeds 100 for the first time
threshold = 100
exceeding_index = np.argmax(cumulative_sum > threshold)

print("Index where cumulative sum exceeds", threshold, ":", exceeding_index)


# ### Task 6 - Performing Linear Algebra Operations (3 points)
# Description: In this task, you will work with a randomly generated 2-dimensional array and perform linear algebra operations using NumPy. You will calculate the determinant of the array, compute its inverse, and verify that the product of the array and its inverse yields the identity matrix. This task provides an opportunity to explore fundamental linear algebra concepts, such as determinants, matrix inverses, and the properties of the identity matrix, using NumPy.
# 
# 1. Create a 2-dimensional array with shape (2, 2) and fill it with random integers between 1 and 9.
# 2. Calculate the determinant of the array.
# 3. Compute the inverse of the array.
# 4. Multiply the array by its inverse.
# 5. Print the final array.

# In[6]:


import numpy as np

# Create a 2-dimensional array with shape (2, 2) and fill it with random integers between 1 and 9
array = np.random.randint(1, 10, size=(2, 2))
print("Original array:")
print(array)

# Calculate the determinant of the array
determinant = np.linalg.det(array)
print("Determinant:", determinant)

# Compute the inverse of the array
inverse = np.linalg.inv(array)
print("Inverse:")
print(inverse)

# Multiply the array by its inverse
result = np.dot(array, inverse)
print("Final array:")
print(result)

