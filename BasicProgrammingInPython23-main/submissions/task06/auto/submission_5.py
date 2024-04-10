#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 6
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Recall of previous concepts.
# 
# ___
# 
# **DEADLINE**:  12th June until 12:15  
# **Your name here**: Sadaf Amirmaki 
# **Your university mail**: samirmaki@uos.de
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

# ## Tuples

# ### Task 1 - City Population Tracker (3 points)
# 
# Write a program that takes a list of cities and their corresponding populations as input. The program should calculate the total population of all the cities and determine the cities with the highest and lowest populations.
# 
# Your program should perform the following steps:
# 
# 1. Define lists, where each list contains the name of a city and its population.
# 2. Use a for loop to iterate over the lists and calculate the total population by adding up the populations of all the cities.
# 3. Use if statements to determine the city with the highest population and the city with the lowest population.
# 4. Print the total population of all the cities, as well as the names and populations of the cities with the highest and lowest populations.
# 
# In this task, you'll need to use lists to store the cities and their populations. You'll iterate over the list using a for loop, perform calculations to determine the total population, and find the cities with the highest and lowest populations using if statements. Finally, you'll print the population summary and the details of the cities with the highest and lowest populations.
# 
# **Hint:** Using lambda function might be useful when finding the cities with the highest and lowest populations.

# In[2]:


# Define an empty list to store city population tuples
cities = []

# Get the number of cities from the user
num_cities = int(input("Enter the number of cities: "))

# Iterate over the range of the number of cities
for i in range(num_cities):
    # Prompt the user for city name and population
    city_name = input(f"Enter the name of city {i+1}: ")
    population = int(input(f"Enter the population of {city_name}: "))

    # Append the city name and population as a tuple to the cities list
    cities.append((city_name, population))

# Calculate the total population
total_population = sum(population for city, population in cities)

# Find the city with the highest population
highest_city = max(cities, key=lambda x: x[1])

# Find the city with the lowest population
lowest_city = min(cities, key=lambda x: x[1])

# Print the population summary
print("\nPopulation Summary:")
print(f"Total population of all cities: {total_population}\n")

# Print the city with the highest population
print("City with the highest population:")
print(f"Name: {highest_city[0]}")
print(f"Population: {highest_city[1]}\n")

# Print the city with the lowest population
print("City with the lowest population:")
print(f"Name: {lowest_city[0]}")
print(f"Population: {lowest_city[1]}")


# ### Task 2 -  Student Grades  (2 points)
# You are a teacher and you need to calculate the average grade for each student in your class. Each student has four subject grades: Math, Science, English, and History. You have a list of tuples, where each tuple contains the student's name followed by their subject grades. Write a program that calculates and prints the average grade for each student in the following format:
# 
# Alice: Average Grade = 88.75
# 
# Bob: Average Grade = 79.0
# 
# Claire: Average Grade = 91.0
# 
# 
# **Instructions:**
# 1. Define a function named ```calculate_average``` that takes a tuple of grades as input and returns the average grade.
# 2. Iterate over each tuple in the grades list.
# 3. Extract the student's name and grades from each tuple.
# 4. Call the ```calculate_average``` function with the grades tuple to calculate the average grade.
# 5. Print the student's name and average grade using the provided format.
# 
# Note: You can assume that each tuple in the list will have the correct format and number of grades.
# 
# This task will test your understanding of tuples, iteration, and function usage. Good luck!

# In[3]:


def calculate_average(grades):
    # Calculate the average grade by summing up the grades and dividing by the number of subjects
    average = sum(grades[1:]) / (len(grades) - 1)
    return average

grades = [("Alice", 85, 90, 92, 88),
          ("Bob", 76, 82, 80, 78),
          ("Claire", 92, 88, 90, 94)]

for student_grades in grades:
    name = student_grades[0]
    average_grade = calculate_average(student_grades)
    print(f"{name}: Average Grade = {average_grade}")


# ## Sets

# ### Task 3 - Set Operations Calculators   (2 points)
# 
# Write a Python program that defines the following functions to perform set operations:
# 
# 1. union(set1, set2): This function takes two sets as input and returns their union.
# 2. intersection(set1, set2): This function takes two sets as input and returns their intersection.
# 3. difference(set1, set2): This function takes two sets as input and returns the difference between the first set and the second set (i.e., elements in set1 that are not present in set2).
# 4. symmetric_difference(set1, set2): This function takes two sets as input and returns their symmetric difference (i.e., elements that are present in either set1 or set2, but not both).
# 
# Your program should then prompt the user to enter the elements of two sets and call the respective functions to perform the set operations. The results should be displayed to the user.

# In[4]:


set1={1, 2, 3, 4} 
set2={3, 4, 5, 6}

def union(set1, set2):
  return set1.union(set2)

def intersection(set1, set2):
  return set1.intersection(set2)

def difference(set1, set2):
  return set1.difference(set2)

def symmetric_difference(set1, set2):
  return set1.symmetric_difference(set2)

# Perform the set operations using the defined functions
set_union = union(set1, set2)
set_intersection = intersection(set1, set2)
set_difference = difference(set1, set2)
set_symmetric_difference = symmetric_difference(set1, set2)

# Display the results
print("Union:", set_union)
print("Intersection:", set_intersection)
print("Difference (Set1 - Set2):", set_difference)
print("Symmetric Difference:", set_symmetric_difference)


# ### Task 4 - Unique Elements Counter   (3 points)
# 
# Write a Python program that defines a function called ```count_unique_elements```  which takes a list as input and returns the count of unique elements in the list and performs the following steps:
# 
# 1. Define the function called ```count_unique_elements```.
# 2. Prompt the user to enter a list of numbers.
# 3. Convert the numbers from strings to integers.
# 4. Call the ```count_unique_elements``` function and display the result.
# 
# **Hint:** List comprehension might help you convert the numbers from strings to integers.

# In[5]:


def count_unique_elements(lst):
    unique_elements = set(lst)  # Convert the list to a set to get unique elements
    return len(unique_elements)  # Return the count of unique elements

# Prompt the user to enter a list of numbers
user_input = input("Enter a list of numbers (separated by spaces): ")

# Split the user input into individual numbers
numbers = user_input.split()

# Convert the numbers from strings to integers
numbers = [int(num) for num in numbers]

# Call the count_unique_elements function and display the result
unique_count = count_unique_elements(numbers)
print("Number of unique elements:", unique_count)


# ## Dictionaries

# ### Task 5 - Book Collection Manager (5 points)
# 
# You are working on a project that requires managing a book collection. You need to create a program that uses a dictionary to store information about the books. Each book will have a unique ID as the key and a dictionary of details as the value. The details of each book include the title, author, and publication year.
# 
# Implement the following functions to interact with the book collection:
# 
# 1. add_book(collection, book_id, title, author, year): Adds a new book to the collection with the given book ID, title, author, and publication year.
# 2. remove_book(collection, book_id): Removes a book from the collection with the given book ID.
# 3. search_book(collection, book_id): Searches for a book in the collection with the given book ID and displays its details (title, author, year) if found.
# 4. display_all_books(collection): Displays the details of all books in the collection.

# In[6]:


def add_book(collection, book_id, title, author, year):
    collection[book_id] = {"title": title, "author": author, "year": year}

def remove_book(collection, book_id):
    if book_id in collection:
        del collection[book_id]

def search_book(collection, book_id):
    if book_id in collection:
        book_details = collection[book_id]
        print("Book Details:")
        print(f"Title: {book_details['title']}")
        print(f"Author: {book_details['author']}")
        print(f"Year: {book_details['year']}")
    else:
        print("Book not found in the collection.")

def display_all_books(collection):
    print("All Books in the Collection:")
    for book_id, book_details in collection.items():
        print(f"Book ID: {book_id}")
        print(f"Title: {book_details['title']}")
        print(f"Author: {book_details['author']}")
        print(f"Year: {book_details['year']}")
        print()

# Create an empty book collection
book_collection = {}

# Perform operations on the book collection
add_book(book_collection, 1, "Python Programming", "John Smith", 2022)
add_book(book_collection, 2, "Data Science Basics", "Alice Johnson", 2021)
add_book(book_collection, 3, "Web Development Guide", "Bob Williams", 2020)

remove_book(book_collection, 2)

search_book(book_collection, 1)
search_book(book_collection, 2)

display_all_books(book_collection)


# ### Task 6 -  Student Grade Tracker   (5 points)
# 
# Create a class called ```StudentGradeTracker``` that represents a grade tracker for students. The class should have the following methods:
# 
# 1. init(self): Initializes an empty dictionary to store student grades.
# 2. add_grade(self, student_id, grade): Adds a grade to the grade tracker for the given student. The student_id should be the key, and the grade should be the value in the dictionary. If the student_id already exists in the grade tracker, print a message indicating that the grade has been updated.
# 3. remove_grade(self, student_id): Removes the grade for the given student from the grade tracker. If the student_id is found and removed, print a message indicating that the grade has been removed. If the student_id is not found in the grade tracker, print a message indicating that the student does not have a grade recorded.
# 4. display_grades(self): Displays all the grades in the grade tracker. If the grade tracker is not empty, print each student's grade on a new line in the format: "Student ID: Grade". If the grade tracker is empty, print a message indicating that no grades have been recorded.
# 
# **Instructions:**
# 
# 1. Implement the StudentGradeTracker class with the methods described above.
# 2. Create an instance of the StudentGradeTracker class.
# 3. Add at least three grades to the grade tracker using the add_grade() method.
# 4. Display all the grades in the grade tracker using the display_grades() method.
# 5. Remove one grade from the grade tracker using the remove_grade() method.
# 6. Display the updated grades in the grade tracker using the display_grades() method.

# In[7]:


class StudentGradeTracker:
    def __init__(self):
        self.grade_tracker = {}

    def add_grade(self, student_id, grade):
        if student_id in self.grade_tracker:
            print(f"Grade updated for student {student_id}")
        self.grade_tracker[student_id] = grade

    def remove_grade(self, student_id):
        if student_id in self.grade_tracker:
            del self.grade_tracker[student_id]
            print(f"Grade removed for student {student_id}")
        else:
            print(f"No grade recorded for student {student_id}")

    def display_grades(self):
        if self.grade_tracker:
            print("Grades:")
            for student_id, grade in self.grade_tracker.items():
                print(f"Student ID: {student_id} - Grade: {grade}")
        else:
            print("No grades recorded.")

# Create an instance of the StudentGradeTracker class
grade_tracker = StudentGradeTracker()

# Add grades to the tracker
grade_tracker.add_grade("001", 85)
grade_tracker.add_grade("002", 92)
grade_tracker.add_grade("003", 78)

# Display the grades
grade_tracker.display_grades()

# Remove a grade
grade_tracker.remove_grade("002")

# Display the updated grades
grade_tracker.display_grades()

