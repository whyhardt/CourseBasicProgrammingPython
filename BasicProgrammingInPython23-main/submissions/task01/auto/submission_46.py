#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 1
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Declaring variables, data types, operations, and if-statements.  
# 
# ___
# **DEADLINE**: 14th May until 23:59  
# **Your name here**: Lotta Müller 
# **Your university mail**: lotmueller@uos.de
# ___
# 
# **Important information**:  
# In order to pass this sheet you need to achieve 10/20 points.  
# For the best possible grade you require 20/20 points, however, since some harder tasks may take a lot of time you don't have to pressure yourself.  
# If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
# Hand in your sheet in studip in the respective folder until the deadline.  
# If you receive no email until a few days after submission you will have passed, the sample solution will also be uploaded around then.  
# If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  

# ## Task 1 Declaring variables (8 points)
# Please declare the following variables with the specific data types and values listed.  
# 
#  a) A string with the value "hello world"  
#  b) An integer with the value "-19"  
#  c) A float with the value "7.29"  
#  d) A boolean value of "False"  
#  e) A tuple containing the integers "1", "2", and the float "4.56"  
#  f) A list containing the string "a", "b", and "c" as elements  
#  g) The truth value of 9 is greater than or equal to 9  
#  h) The result of 28 times 2 minus 14  

# In[4]:


a = 'hello world'
b = int(-19)
c = float(7.29)
d = bool(19>22)
e = (1, 2, float(4.56))
f = ['a','b','c']
g = bool(9>=9)
h = int(28*2-14)
print(a, b, c, d, e, f, g, h)


# ## Task 2 Implementing formulas (4 points)
# Please implement mathematical formulas in the cells below.  
# You are given four variables ```a``` ```b``` ```c```, and ```d``` at the start, and can chose any float or integer value for them to test your formula.  
# Note however that, depending on what you chose, you may run into division by zero errors or a negative squareroot, so chose carefully if you wish to change these.

# In[ ]:


a = 1
b = 2
c = 5.37
d = 7.92


# ### Formula 1
# $\frac{A+B}{C+D}$  
# "A plus B divided by C plus D"

# ## Formula 2zz

# In[2]:


a=2
b=6
c=3
d=1
formula=(a+b)/(c+d)
print(formula)


# ### Formula 3
# $\frac{A^2+B^3}{1+\frac{C}{D}}$  
# "A to the power of 2 plus B to the power of 3, divided by 1 plus the quotient of C and D"

# In[8]:


a=4
b=2
c=6
d=3
formula3=((a**2+b**3)/(1+(c/d)))
print(formula3)


# ### Formula 4
# $\sqrt[2]{A-B}$  
# "The square root of A minus B"  
# **Hint:** You can use the power of 1/2 instead here.

# In[10]:


a=11
b=2
formula4=(a-b)**(1/2)
print(formula4)


# ## Task 3 Variables - Value Switching (3 points)
# 
# Write a program that asks the user to enter two different numbers and then switches the values that are stored in a and b. Print the switched values as an output.
# 
# **Hint:** You may need to look up ```input()``` function to gather information from the users.

# In[1]:


a=int(input(3)) #enter number

b=int(input(7)) #enter number
print('a=',b, 'b=',a)


# In[ ]:





# ## Task 4 If statements (5 points)
# Imagine that you are working at a theme park and selling tickets for the rollercoaster.  
# You are obliged to ask all visitors about their height (in cm) before selling them any tickets.  
# If they are 120cm or taller than that, then they are allowed to ride the rollercoaster and you need to ask how old they are.  
# Depending on their age, the amount that they have to pay differs:
# 
# * If they are younger than 12: 5€
# * If they are 18 or younger: 8€
# * If they are older than 18: 15€
# 
# Depending on the result change the value of the variables price (int) and allowed (bool) to match the specified conditions!
# 
# **Hint:** Do not forget to inform the visitors shorter than 120cm that they cannot ride the rollercoaster at the moment.  
# You can adjust the code in the cell below to or use the input statement which is commented out to test for specific height and age combinations.  
# If someone is not allowed on the ride, then you do not need to give them a price obviously.

# In[ ]:


height = 160
age = 19

#alternatively comment this out and input
# print("Height:")
# height = int(input())
# age = int(input())


# In[ ]:


height=int(input())
160
age=int(input())
19
if height>=120:
     if age<12:
             print('allowed to ride, price: 5 euros')
     elif age<18:
             print('allowed to ride, price: 8 euros')
     else:
             print('allowed to ride, price: 15 euros')
 else:
     print('sorry, you\'re too short')


# In[ ]:


print(f'The person (height={height},age={age}) is {"not" if not allowed else ""} allowed to take the ride and their price is {price}€')


# In[ ]:




