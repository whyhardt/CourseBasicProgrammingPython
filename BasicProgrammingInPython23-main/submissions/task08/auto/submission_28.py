#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 8
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Matplotlib.
# 
# ___
# 
# **DEADLINE**: 23rd June until 12:15  
# **Your name here**: Leonard Schwanke  
# **Your university mail**: lschwanke@uos.de
# 
# ___
# 
# **Important information**:  
# In order to pass this sheet you need to achieve 10/20 points.
# For the best possible grade you require 20/20 points, however, since some harder tasks may take a lot of time you don't have to pressure yourself. 
# If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
# Hand in your sheet in studip in the respective folder until the deadline.  
# If you receive no email until a few days after submission you will have passed, the sample solution will also be uploaded around then.  
# If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  

# ### Task 1 - Temperature Plot (2 points)
# 
# Implement a line plot that visualizes temperature variations over a week:
# 
# - x-axis should store the days of the week (e.g., Monday, Tuesday, etc.).
# - y-axis should store the temperature values in degrees Celsius.
# - For the y-axis, you need to generate random temperature values between 20 and 30 for each day.
# - The line color should be set to purple.
# - The title of the plot should be "Weekly Temperature".
# - Label the x-axis as "Days of the Week" and the y-axis as "Temperature (°C)".

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

temperature = np.random.uniform(20, 30, len(days))

plt.plot(days, temperature, color='purple')
plt.title('Weekly Temperature')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')

plt.show()


# ### Task 2 - Steps Taken Analysis (4 points)
# 
# You have a dataset that records the number of steps taken each day of the week by three students: Alice, Bob, and Carol. Your task is to create a scatter plot to visualize the steps taken and then enhance the plot by adding a legend and connecting the scatterplot points with a line.
# 
# Write a Python code snippet using Matplotlib to accomplish the following tasks:
# 
# 1. Create a scatter plot using Matplotlib, with the weekdays on the x-axis and the number of steps on the y-axis. Make sure to label the axes appropriately.
# 2. Customize the scatter plot by setting the marker style and color of the points for each student to distinguish them. Use a different marker style and color for each student. 
# 3. Add a legend to the plot to indicate the meaning of the different marker colors or styles. Make sure to provide clear labels for each student category in the legend.
# 4. Connect the scatterplot points with a line to visualize the trend in the number of steps throughout the weekdays. The line should pass through each data point.
# 5. Customize the line by setting the color, style, and width to make it clearly visible.
# 6. Add a title to the plot to describe the steps taken throughout the weekdays.
# 
# Your task is to complete the code by replacing the blank spaces with the appropriate code to accomplish the given tasks.

# In[2]:


import matplotlib.pyplot as plt

# Steps taken each day of the week for 3 students
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
alice_steps = [5000, 6000, 4500, 7000, 5500]
bob_steps = [4000, 5500, 6000, 4500, 5000]
carol_steps = [5500, 6500, 4000, 5500, 6000]

# Scatter plot
plt.scatter(weekdays, alice_steps, marker='o', color='red', label='Alice')
plt.scatter(weekdays, bob_steps, marker='s', color='blue', label='Bob')
plt.scatter(weekdays, carol_steps, marker='^', color='green', label='Carol')

# Line connecting scatterplot points
plt.plot(weekdays, alice_steps, color='red', linestyle='-', linewidth=1)
plt.plot(weekdays, bob_steps, color='blue', linestyle='-', linewidth=1)
plt.plot(weekdays, carol_steps, color='green', linestyle='-', linewidth=1)

# Legend
plt.legend()

# Axes labels and title
plt.title('Steps Taken Throughout the Week')
plt.xlabel('Weekdays')
plt.ylabel('Number of Steps')

# Display the plot
plt.show()


# ### Task 3 - Math Exam Score Distribution (8 points)
# 
# You have the scores of two students from a math exam. Your task is to create histogram plots to visualize the distribution of their scores. Additionally, you need to customize the histogram plots by adjusting the bin sizes and create two histogram plots side by side for comparison.
# 
# Write a Python code snippet using Matplotlib to accomplish the following tasks:
# 
# 1. Create a dataset with the math exam scores for two students.
# 2. Create two separate histogram plots using Matplotlib, one for each student's scores.
# 3. Customize the appearance of the histogram plots by adjusting the bin sizes to visualize the distribution more accurately.
# 4. Display both histogram plots side by side for easy comparison.
# 5. Your code should include appropriate axis labels, a title for each histogram plot, and a legend to differentiate the two students.
# 
# Example output:
# 
# [Histogram plot 1] 
# * Title: Student 1 Math Exam Score Distribution
# * X-axis label: Scores
# * Y-axis label: Frequency
# 
# [Histogram plot 2]
# * Title: Student 2 Math Exam Score Distribution
# * X-axis label: Scores
# * Y-axis label: Frequency
# 
# Note: Make sure to customize the bin sizes to suit the range and distribution of the scores for each student.

# In[18]:


# Generate sample scores for two students
student1_scores = np.random.normal(70, 10, 100)  # Mean: 70, Standard Deviation: 10
student2_scores = np.random.normal(80, 8, 100)   # Mean: 80, Standard Deviation: 8

# Set the bin sizes for the histograms
bin_size_student1 = 4
bin_size_student2 = 4

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Plot histogram for Student 1
axes[0].hist(student1_scores, bins=range(50, 101, bin_size_student1), color='blue', alpha=0.7)
axes[0].set_title("Student 1 Math Exam Score Distribution")
axes[0].set_xlabel("Scores")
axes[0].set_ylabel("Frequency")

# Plot histogram for Student 2
axes[1].hist(student2_scores, bins=range(50, 101, bin_size_student2), color='green', alpha=0.7)
axes[1].set_title("Student 2 Math Exam Score Distribution")
axes[1].set_xlabel("Scores")
axes[1].set_ylabel("Frequency")

# Add a legend to differentiate the two students
fig.legend(["Student 1", "Student 2"])

# Adjust spacing between subplots
fig.tight_layout()

# Display the histogram plots
plt.show()


# ### Task 4 - Stacked Bar Plot (6 points)
# 
# Create a stacked bar plot to display the distribution of sales revenue for a company across different regions and product categories:
# 
# - Given the ```regions```, ```categories``` and ```revenue```, you should gather the sales revenue data for each region and product category.
# - Plot a stacked bar plot where each bar represents a region, and the stacked segments within the bar represent the revenue for each product category.
# - Customize the plot by setting colors for each product category: ```red``` for electronics, ```green``` for clothing and ```blue``` for books. Then, add a legend to display these three color-product pairs.
# - Add a title ```"Sales Revenue by Region and Product Category"```.
# - Label the x-axis and y-axis as  ```Regions``` and ```Revenue```, respectively.

# In[19]:


import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Books']

revenue = np.array([[100, 200, 150],
                    [150, 120, 80],
                    [80, 100, 200],
                    [180, 120, 90]])

plt.bar(regions, revenue[:, 0], bottom=np.sum(revenue[:, :0], axis=1), color='red')
plt.bar(regions, revenue[:, 1], bottom=np.sum(revenue[:, :1], axis=1), color='green')
plt.bar(regions, revenue[:, 2], bottom=np.sum(revenue[:, :2], axis=1), color='blue')

plt.title('Sales Revenue by Region and Product Category')
plt.xlabel('Regions')
plt.ylabel('Revenue')
plt.legend(categories)

