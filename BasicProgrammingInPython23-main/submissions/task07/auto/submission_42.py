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
# **Your name here**: Nina Beckers 
# **Your university mail**: nbeckers@uos.de
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

# Create a 1D array of size 10 with random integer values between 1 and 100
arr = np.random.randint(1, 101, 10)

# Reshape the array into a 2x5 matrix
arr_reshaped = np.reshape(arr, (2, 5))

# Transpose the matrix
arr_transposed = np.transpose(arr_reshaped)

# Find the index of the maximum value in the array
max_index = np.argmax(arr)

# Print the original array
print(f"The original array:\n{arr}")

# Print the reshaped array
print(f"The reshaped array:\n{arr_reshaped}")

# Print the transposed array
print(f"The transposed array:\n{arr_transposed}")

# Print the index of the maximum value
print(f"The index of the maximum value:\n{max_index}")


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
arr1 = np.random.randn(100)

# Split the array into positive and negative elements
positive_array = arr1[arr1 >= 0]
negative_array = arr1[arr1 < 0]

# Calculate the standard deviations
positive_std_dev = np.std(positive_array)
negative_std_dev = np.std(negative_array)

# Calculate the standard deviation ratio
sdr = positive_std_dev / negative_std_dev

# Print the original array
print(f"Array:\n{arr1}")

# Print the positive array
print(f"The positive array:\n{positive_array}")

# Print the negative array
print(f"The negative array:\n{negative_array}")

# Print the standard deviation ratio
print(f"Standard Deviation Ratio:\n{sdr}")


# ### Task 3 - Identity Matrix (3 points)
# 
# Create a 5x5 identity matrix where:
# 
# - All diagonal elements are equal to 0.
# - The rest of the elements should be random integers between 0 and 50 (inclusive).

# In[8]:


import numpy as np

# Create a 5x5 identity matrix
identity_matrix = np.zeros((5, 5))

# Generate random integers between 0 and 50 (inclusive)
random_integers = np.random.randint(0, 51, size = (5, 5))

# Replace the non-diagonal elements with random integers
identity_matrix[~np.eye(5, dtype=bool)] = random_integers[~np.eye(5, dtype=bool)]

print(identity_matrix)


# ### Task 4 - Calculate the Euclidean distance between two arrays (2 points)
# The Euclidean distance measures the straight-line distance between two points in space. In this task, you will calculate the Euclidean distance between two 1-dimensional arrays using the NumPy library.
# 
# **Hint:** To calculate the Euclidean distance between the two arrays, we can use the np.linalg.norm() function. This function calculates the norm, which is a generalized form of the Euclidean distance, of the difference between the arrays:
# 

# In[9]:


import numpy as np

# Create two 1-dimensional arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Calculate the difference between the two arrays
difference = arr2 - arr1

# Calculate the Euclidean distance using the norm function from the linalg module
distance = np.linalg.norm(difference)

# Print the calculated Euclidean distance
print("Euclidean Distance:", distance)


# ### Task 5 - Find the Point of Exceeding a Cumulative Sum Threshold (4 points)
# 
# Generate a random 1-dimensional array of size 100 with values ranging from 0 to 9. Calculate the cumulative sum of the array and find the index where the cumulative sum exceeds 100 for the first time, then print the index.
# Description:
# In this task, you will work with a randomly generated 1-dimensional array of numerical values. Your goal is to calculate the cumulative sum of the array, which represents the running total of the values. Then, you need to identify the position in the array where the cumulative sum exceeds a specific threshold.

# In[10]:


import numpy as np

# Generate a random 1-dimensional array of size 100 with values ranging from 0 to 9
arr = np.random.randint(0, 10, size=100)

# Calculate the cumulative sum of the array
cumulative_sum = np.cumsum(arr)

# Set the threshold value
threshold = 100

# Find the index where the cumulative sum first exceeds the threshold
index = np.argmax(cumulative_sum > threshold)

# Print the index where the cumulative sum exceeds the threshold
print("Index where cumulative sum exceeds", threshold, ":", index)


# ### Task 6 - Performing Linear Algebra Operations (3 points)
# Description: In this task, you will work with a randomly generated 2-dimensional array and perform linear algebra operations using NumPy. You will calculate the determinant of the array, compute its inverse, and verify that the product of the array and its inverse yields the identity matrix. This task provides an opportunity to explore fundamental linear algebra concepts, such as determinants, matrix inverses, and the properties of the identity matrix, using NumPy.
# 
# 1. Create a 2-dimensional array with shape (2, 2) and fill it with random integers between 1 and 9.
# 2. Calculate the determinant of the array.
# 3. Compute the inverse of the array.
# 4. Multiply the array by its inverse.
# 5. Print the final array.

# In[11]:


import numpy as np

# Generate a random 2-dimensional array with shape (2, 2) and random integers between 1 and 9
arr = np.random.randint(1, 10, size=(2, 2))

# Calculate the determinant of the array
determinant = np.linalg.det(arr)

# Compute the inverse of the array
inverse = np.linalg.inv(arr)

# Multiply the array by its inverse to obtain the identity matrix
identity = np.dot(arr, inverse)

# Print the resulting identity matrix
print("Identity Matrix:\n", identity)


# In[ ]:




