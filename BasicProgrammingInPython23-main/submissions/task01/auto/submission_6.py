#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 1
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Declaring variables, data types, operations, and if-statements.  
# 
# ___
# **DEADLINE**: 14th May until 23:59  
# **Your name here**: Miguel Angel Prieto-Castellanos  
# **Your university mail**: mprietocaste@uni-osnabrueck.de
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

# In[49]:


a = "hello world"
print("a)", a, type(a))
b = -19
print ("b)", b, type(b))
c = 2.3
print("c)", c, type(c))
d = False or True
print("d)", d, type(d))
e = (1, 2, 4.56)
print ("e)", e, type(e))
f = ["a", "b", "c"]
print("f)", f, type(f))
g = bool((9 > 9) or (9==9))
print("g)", g, type(g))
h = (28*2)-14
print("h)", h, type(h))


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

# In[9]:


(a+b) / (c+d)


# ## Formula 2
# $\frac{A+B+C+D}{4}$  
# "The sum of A, B, C, and D, divided by four"

# In[7]:


(a+b+c+d) / 4


# ### Formula 3
# $\frac{A^2+B^3}{1+\frac{C}{D}}$  
# "A to the power of 2 plus B to the power of 3, divided by 1 plus the quotient of C and D"

# In[8]:


((a**2) + (b ** 3)) / (1 + (c / d))


# ### Formula 4
# $\sqrt[2]{A-B}$  
# "The square root of A minus B"  
# **Hint:** You can use the power of 1/2 instead here.

# In[6]:


(a-b)*(1/2)


# ## Task 3 Variables - Value Switching (3 points)
# 
# Write a program that asks the user to enter two different numbers and then switches the values that are stored in a and b. Print the switched values as an output.
# 
# **Hint:** You may need to look up ```input()``` function to gather information from the users.

# In[51]:


#I changed "a" and "b" for "q" and "r" because I already used them in Task 1 :)

r = input ('enter the number of eyes a person usually has ')
q = input ('enter the number of brains a person usually has ')

print("r = " + r)
print("q = " + q)


# In[52]:


print ("what if it were the other way around?")

#swithing numbers...

r,q = q,r

print("r = ", r)
print("q = ", q)
print ("fascinating creature...")

#I'm not known for my jokes...


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

# In[121]:


#(please use my form in below :)
#height : 160
#age : 19 
#allowed : True 
#price = 15

#alternatively comment this out and input
# print("Height:")
# height = int(input())
# age = int(input())


# In[49]:


height = input("digit the client height in cms ")
height = int(height)

if ((height > 120) or (height == 120)):
    allowed = True
    age = input("digit the client age ")
    age = int(age)
    if (age < 12):
        price = 5
    elif (age < 18):
        price = 8
    elif (age > 18):
        price = 15
    print("The person with height", height, "cm and age", age, "is allowed to ride the roller coaster. Price:", price, "€")
else:
    print("sorry, you are not allowed to ride today")


# In[50]:


#I had some trouble adjusting the final verification message, I figured out this one which works (although is not as elegant)

if ((height > 120) or (height == 120)):
    print("The person with height", height, "cm and age", age, "is allowed to ride the roller coaster. Price:", price, "€")
else:
    print("The person with height", height, "is not allowed to ride the roller coaster today.")


# In[ ]:





# In[ ]:




