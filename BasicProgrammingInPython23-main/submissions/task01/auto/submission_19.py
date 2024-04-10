#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Coding Tasks - Week 1
Welcome to the Python Programming Exercise Sheet!  
In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
Topics covered are: Declaring variables, data types, operations, and if-statements.  

___
**DEADLINE**: 14th May until 23:59  
**Your name here**: Razieh Malihi  
**Your university mail**: rmalihi@uni-osnabrueck.de
___

**Important information**:  
In order to pass this sheet you need to achieve 10/20 points.  
For the best possible grade you require 20/20 points, however, since some harder tasks may take a lot of time you don't have to pressure yourself.  
If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
Hand in your sheet in studip in the respective folder until the deadline.  
If you receive no email until a few days after submission you will have passed, the sample solution will also be uploaded around then.  
If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  


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

# In[3]:


a = "hello world"
b = -19
c = 7.29
d =False
e = (1,2,4.56)
f = ["a","b","c"]
g = 9>=9
h = 28*2-14
print(h)


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

# In[10]:


A = 1
B = 2
C = 5.37
D = 7.92
print((A+B)/(C+D))


# In[11]:


A=2
B=4
C=1
D=2
print((A+B)/(C+D))


# ## Formula 2
# $\frac{A+B+C+D}{4}$  
# "The sum of A, B, C, and D, divided by four"

# In[12]:


A = 1
B = 2
C = 5.37
D = 7.92
print((A+B+C+D)/4)


# In[13]:


A = 2
B = 3
C = 4
D = 3
print((A+B+C+D)/4)


# ### Formula 3
# $\frac{A^2+B^3}{1+\frac{C}{D}}$  
# "A to the power of 2 plus B to the power of 3, divided by 1 plus the quotient of C and D"

# In[16]:


A = 1
B = 2
C = 5.37
D = 7.92
print(((A**2)+(B**3))/(1+(C//D)))


# In[18]:


A = 1
B = 2
C =2
D = 1
print(((A**2)+(B**3))/(1+(C//D)))


# ### Formula 4
# $\sqrt[2]{A-B}$  
# "The square root of A minus B"  
# **Hint:** You can use the power of 1/2 instead here.

# 

# In[20]:


A = 1
B = 2
print((A-B)**.5)


# In[21]:


A = 8
B = 4
print((A-B)**.5)


# ## Task 3 Variables - Value Switching (3 points)
# 
# Write a program that asks the user to enter two different numbers and then switches the values that are stored in a and b. Print the switched values as an output.
# 
# **Hint:** You may need to look up ```input()``` function to gather information from the users.

# In[9]:


a=input("a:")
b=input("b:")
a,b=b,a
print("a:",a,  "b:",b)


# In[ ]:


## Task 4 If statements (5 points)
Imagine that you are working at a theme park and selling tickets for the rollercoaster.  
You are obliged to ask all visitors about their height (in cm) before selling them any tickets.  
If they are 120cm or taller than that, then they are allowed to ride the rollercoaster and you need to ask how old they are.  
Depending on their age, the amount that they have to pay differs:

* If they are younger than 12: 5€
* If they are 18 or younger: 8€
* If they are older than 18: 15€

Depending on the result change the value of the variables price (int) and allowed (bool) to match the specified conditions!

**Hint:** Do not forget to inform the visitors shorter than 120cm that they cannot ride the rollercoaster at the moment.  
You can adjust the code in the cell below to or use the input statement which is commented out to test for specific height and age combinations.  
If someone is not allowed on the ride, then you do not need to give them a price obviously.


# In[19]:


x=input("your height in cm:")
y=input("your age:")
if int(x)>=120:
    if int(y)< 12:
        print(" allowed to take the ride and their price is  5€")
    elif 12<=int(y)<18:
        print("allowed to take the ride and their price is  8€")
    elif int(y)>18:
        print("allowed to take the ride and their price is  15€")
else:
    print("not allowed to take the ride")

    
    



# In[ ]:


#add here


# In[ ]:


print(f'The person (height={height},age={age}) is {"not" if not allowed else ""} allowed to take the ride and their price is {price}€')


# In[ ]:




