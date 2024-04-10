#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 4
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Functions, recursion and variable scope.
# 
# ___
# **DEADLINE**: 29th May until 12:15  
# **Your name here**: Maxine Breede   
# **Your university mail**: mbreede@uos.de
# ___
# 
# **Important information**:  
# In order to pass this sheet you need to achieve 10/20 points.  
# For the best possible grade you require 20/20 points, however, since some harder tasks may take a lot of time you don't have to pressure yourself.  
# If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
# Hand in your sheet in studip in the respective folder until the deadline.  
# If you receive no email until a few days after submission you will have passed, the sample solution will also be uploaded around then.  
# If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  

# ## Task 1 Simple mathematical functions (2 points)
# ### Sum function
# Write a function that takes different numbers as parameters, and returns the sum of all numbers.  
# The function should be called ```get_sum``` and take in four numbers in the form of four parameters.  
# Make sure to also test your function below to check if it works properly.

# In[1]:


def get_sum(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4


# In[2]:


get_sum(1,2,3,4)


# ### Area of a circle
# Write a function ```circle_area``` which takes in the radius of a circle as a float number.  
# Using ```pi```, as imported from the math module ```math``` may be helpful here.  
# Remember the formula for getting the area from a circle with known radius is $A=\pi r^2$.  

# In[15]:


from math import pi
print(pi)


# In[16]:


def circle_area(radius):
    area = pi * radius ** 2
    return area


# In[17]:


circle_area(2.34)


# ## Task 2 Recall of  loops and lists (3 poins)
# Write a function ```intersection``` which receives two lists as arguments and returns another list containing all items that are present in both lists.  
# For example, giving it a list ```[1,2,3,4]``` and a list ```[3,4,5,6]``` should return ```[3,4]```.  

# In[5]:


def intersection(list_a, list_b):
    return list(set(list_a) & set(list_b))


# In[6]:


list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection(list_a, list_b)  


# ## Task 3 Vowel removal (4 points)
# Write a function ```remove_vowels``` that takes a string as input and returns a modified string with all the vowels removed.  
# Vowels are the letters "a", "e", "i", "o", and "u".  
# The output string should have all the remaining characters in the original string, but without any vowels.  
# This task requires knowledge of string manipulation and the use of functions to perform specific tasks on a string.  
# 
# **Hint:** The function should be designed to remove all occurrences of these letters, regardless of whether they are capitalized or lowercase.

# In[7]:


def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string if char not in vowels)


# In[8]:


my_str=input("Enter a text to remove the vowels:")
remove_vowels(my_str)


# ## Task 4 Prime Number Checker (5 points)
# 
# Write a function ```is_prime``` that takes a number as input and returns ```True``` if the number is a prime number, and ```False``` otherwise.  
# **Hint:** A prime number is a number that is only divisible by 1 and itself. Also note that 0 and 1 are not prime numbers.

# In[9]:


def is_prime(number):
    # 0 and 1 are not prime numbers
    if number < 2:  
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# In[10]:


is_prime(5)


# ## Task 5 Recursion (6 points)
# ### Calculating the nth Fibonacci Number Using Recursion (3/6 points)
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. In this question, we will focus on calculating the nth Fibonacci number using recursion. Write a recursive function **fibonacci** that takes an input **n** and returns the nth Fibonacci number. Assume that the Fibonacci sequence starts with 0 as the 1st number and 1 as the 2nd number.   
# To solve this problem using recursion, we break it down into smaller subproblems. For any value of n, the nth Fibonacci number can be obtained by summing the (n-1)th and (n-2)th Fibonacci numbers.
# 
# **Hint:** Remember to cover both the recursive case and the base case, else you end up with an infinite loop.

# In[11]:


def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# In[12]:


n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")


# ### Greatest common divisor (3/6 points)
# Write a function ```gcd``` that takes in two integers and returns their greatest common divisor.  
# The greatest common divisor is the integer that will result in a remainder of zero if used as divisor for both integers.  
# If the gcd is "c", and we have two numbers "a" and "b", then both "remainder of a divided by c" and "remainder of b divided by c" will yield 0.  
# 
# In case you don't know what the concept of greatest common divisor is, feel free to read this explanation or search [here](https://en.wikipedia.org/wiki/Greatest_common_divisor).
# 
# Submitting any working solution will give you three points, submitting a working solution with recursion will give you four.
# 
# **Explanation for a recursive solution**  
# Since this task is a bit harder, we will actually give you, in text, the idea of the recursion in the algorithm.  
# Given a call with the values ```gcd(a, b)```, if you were to do a recursive call with ```gcd(b, a % b)``` every time you have not found a common divisor, you will eventually arrive at one.  
# Think of the following cases to see why:
# 
# ---
# Same number case, the gcd is either of the two numbers:  
# (a=10,b=10, resulting in 10 % 10 = 0, yielding gcd=10)
# 
# ---
# One-sided case (working direction):  
# (a=15, b=5, resulting in 15 % 5 = 0, yielding gcd=5)
# 
# ---
# One-sided case (non-working direction):  
# (a=5, b=15, resulting in 5 % 15 = 5, we now switch around a and b if we call gcd(b, a % b))  
# (a=15, b=5, resulting in 15 % 5 = 0, yielding gcd=5)
# 
# ---
# Unresolved case (neither direction works yet):  
# (a=168, b=20, resulting in 168 % 20 = 8, then we call gcd(20, 8))  
# (a=20, b=8, resulting in 20 % 8 = 4, then we call gcd(8, 4))  
# (a=8, b=4, resulting in 8 % 4 = 0, then we call gcd(4, 0))
# 
# ---
# **All these cases have in common that they, in the end, yield 0 for b and a value for a, take from that information what you want for the base case ;)**

# In[13]:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# In[14]:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD of", a, "and", b, "is:", gcd(a, b))


# In[ ]:




