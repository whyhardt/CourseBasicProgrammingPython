#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 5
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: Object oriented programming (OOP).
# 
# ___
# 
# **DEADLINE**: 5th June until 12:15  
# **Your name here**: Maedeh Amini 
# 
# **Your university mail**: mamini@uni-osnabrueck.de
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

# ## Imports
# From now on you will encounter an import cell here in the top which you should **always** execute first to import necessary libraries for later.  
# 
# Additionally, we want to provide you with a rundown of how imports work since it is related to classes and methods.  
# Imports always consist of either a full or a partial import, full imports are written like ```import library```, partial imports are written like ```from library import Class```.  
# 
# You can think of libraries as separate python scripts from which you import code written, if you say ```from myscript import ThisClass```, what you are essentially doing is run the ```ThisClass``` class definition part of the script ```myscript.py```.  
# 
# Many libraries are built-in and do not require installing such as ```math```, ```re``` (regex), or ```time```.  
# Others, like ```numpy```, ```pandas```, or ```tensorflow```, require an installation via pip or another method.  
# 
# Additionally, you can use ```as``` and ```,``` in your imports.  
# If you type ```import numpy as np``` for instance, then you do not have to type ```numpy.array```, but rather just ```np.array``` which can be a useful abbreviation or be used to rename something important if you have two functions with the same name.  
# 
# If you do ```from datetime import datetime, timedelta``` for example, you are selecting specifically the part ```datetime``` and ```timedelta``` only from the ```datetime``` library. 
# 
# You may even do something like ```from library import Function as anothername```.  
# 
# We hope this explanation helps you with formulating and understanding import statements.  

# In[ ]:


from datetime import datetime, timedelta
from math import pi, sqrt


# ## Task 1 - Creating a Student Class (6 points)
# 
# Create a Python class called ```Student``` which should take the following attributes: ```name```, ```age```, and ```grade```.
# After you define the class, implement the methods ```get_name()```, ```get_age()```, and ```get_grade()``` to access these attributes.  
# 
# You will have to write the whole class from scratch here, then in the cell right below, create an instance of the class and name it ```student```.  
# Finally, you can execute the third code cell which is already pre-written code to retrieve the attributes of the class from your written getter-methods.  
# 
# **Hint:** You will need to define a ```__init__()``` method to be able to receive three arguments or a tuple which represents the three arguments.  
# Additionally, you will need three getter-methods which **return** the value of a certain attribute of the class.  
# 
# **Note:** This is more like a toy task honestly, in reality you would not use getters for simple attributes like this and you could also write a ```__repr__``` or a ```__str__``` method to make the instance print it's attributes, this is mainly for practice. ;)

# In[ ]:


#write your class here
class Student:


# In[ ]:


student = #create an instance here
def __init__ (student, name, age, grade):
    student.name=name
    student.age=age
    student.grade=grade


# In[2]:


class Student:
    def __init__ (student, name, age, grade):
        student.name=name
        student.age=age
        student.grade=grade

    def __str__(student):
        return f"""
           Student name: {student.name} 
           Student age: {student.age}
           Student grade: {student.grade}
           """

s= Student("Sara", 20, 3)
print(s)


# ## Task 2 - Bank Account Class (5 points)

# Create a class called ```BankAccount```  with the following:  
# 
# - It should have the attributes: ```account_number``` and ```balance```.  
# - The dunder methods: ```__init__``` and ```__str__```.  
# - The methods: ```deposit(amount)``` and ```withdraw(amount)```.  
# - Initialisation method: ```__init__(self, account_number, balance)``` which sets the attributes ```account_number``` and ```balance```.  
# - String conversion method; also known as print method: ```__str__(self)``` which simply returns the string ```f'The account {self.account_number} has a balance of {self.balance}.'```.  
# - Deposit method: ```deposit(self, amount)``` which takes an amount (int) as input and adds it to the current balance (attribute) of the account.  
# - Withdrawal method: ```withdraw(self, amount)``` which takes an amount (int) as input and subtracts it from the current balance of the account, if sufficient funds are available, else it will return the string ```"Insufficient funds."```.
# 
# **Note:** Here for the "Insufficient funds" case of the withdrawal method one could also raise a custom error named, for example, InsufficientFundsError. This is not needed and not wanted here, but this is something for you to think about in case you in the future encounter this situation where it makes sense to implement an error for certain cases with classes.

# In[16]:


class BankAccount:
    def __init__(account, account_number, balance):
        account.account_number=account_number
        account.balance=balance

    def __str__(account):
        return f"""
            BankAccount account_number= {account.account_number}
            BankAccount balance= {account.balance}
            """
    
    def deposit(account):
        deposit= int(input("Enter a deposit:"))
        return account.balance + deposit 
    
    def __str__(account):
            return f"""
                    Balance after deposit: {account.balance}
                    """  

    def withdraw(account):
        withdraw = int(input("Enter a withdrawal:"))
        return account.balance-withdraw

    def __str__(account):
            if int(account.balance)< 0:
                print("Insufficient Funds")
            else:
                return f"""
                        Balance after withdrawal: {account.balance}
                        """  
            

A= BankAccount(123456789, 500)
print(A)


# In[ ]:


#Create a BankAccount instance
account = BankAccount("123456789")

#Display the initial balance (str method)
print(account)

#Perform a deposit
account.deposit(1000)

#Display the updated balance
print("Balance after deposit:", account.balance)

#Perform a withdrawal
account.withdraw(500)

#Display the final balance
print("Balance after withdrawal:", account.balance)

#Try to withdraw too much
print(account.withdraw(10000))


# ## Task 3 - Geometric Classes (5 points)
# Finish the following three geometric classes by implementing the four missing statements in the methods.  
# 
# - Rectangle: Implement the missing statement in the ```perimeter``` and ```area``` method.  
# - Triangle: Implement the missing statement in the ```__init__``` method and the equilateral test in the ```is_equilateral``` method.  
# - Circle: Implement the missing statement in the ```diameter``` method.
# 
# **Hint:** For the triangle you may want to look up the ```max``` function and for the rest you can get away with very simple mathematics, you can also look at the internet to get the formulas if you don't know them by heart.

# In[25]:


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return (width+height)*2 
    
    def area(self):
        return width*height


# In[24]:


class Triangle:
    def __init__(self, a, b, c):
        #Triangles, given three lenghts, are only possible if any two side lenghts are greater than the third (check triangle inequality theorem)
        if not ((a+b > c) and (b+c > a) and (a+c > b)):
            raise ValueError(f"The three lengths {a}, {b}, and {c} cannot form a triangle together.")
            
        self.a = a
        self.b = b
        self.c = c
        
        #The width of a traingle is the length of the longest side (use the max function over a list of all side attributes [self.a,self.b,self.c])
        self.width = max(self.a, self.b, self.c) #implement width formula here
        
        #The height of a triangle is calculated, for all known sides, via the formula given here
        self.height = 0.25*self.width*sqrt(sum([self.a,self.b,self.c]))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        return 0.5*self.width*self.height
    
    def is_equilateral(self):
        #A triangle is equilateral if two sides have the same length
        if (width == height): #implement equilateral test here
            return True #the triangle is equilateral
        
        else:
            return False #the triangle is not equilateral


# In[22]:


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return self.radius*pi
    
    def area(self):
        return self.radius*pi**2
    
    def diameter(self):
        return self.radius*2 #implement method here


# In[31]:


# Create an instance of the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return (self.width+self.height)*2 
    
    def area(self):
        return self.width*self.height


# Calculate and print the perimeter of the rectangle
    def __str__ (self):
        return f"""
                Perimeter: {rectangle.perimeter()}
                Area: {rectangle.area()}
                """

rectangle = Rectangle(5, 3)
print(rectangle)


# In[ ]:


# Create an instance of the Triangle class

class Triangle:
    def __init__(self, a, b, c):
        #Triangles, given three lenghts, are only possible if any two side lenghts are greater than the third (check triangle inequality theorem)
        if not ((a+b > c) and (b+c > a) and (a+c > b)):
            raise ValueError(f"The three lengths {a}, {b}, and {c} cannot form a triangle together.")
            
        self.a = a
        self.b = b
        self.c = c
        
        #The width of a traingle is the length of the longest side (use the max function over a list of all side attributes [self.a,self.b,self.c])
        self.width = max(self.a, self.b, self.c) #implement width formula here
        
        #The height of a triangle is calculated, for all known sides, via the formula given here
        self.height = 0.25*self.width* sqrt(sum([self.a,self.b,self.c]))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        return 0.5*self.width*self.height
    
    def is_equilateral(self):
        #A triangle is equilateral if two sides have the same length
        if (width == height): #implement equilateral test here
            return True #the triangle is equilateral
        
        else:
            return False #the triangle is not equilateral

    def __str__ (self):
        return f"""
                Width: {triangle_a.width}
                Height: {triangle_a.height}
                Perimeter: {triangle_a.perimeter()}
                Area: {triangle_a.area()}
                The triangle is equilateral: {triangle_a.is_equilateral()}
                """
    def __str__ (self):
        return f"""
                Width: {triangle_b.width}
                Height: {triangle_b.height}
                Perimeter: {triangle_b.perimeter()}
                Area: {triangle_b.area()}
                The triangle is equilateral: {triangle_b.is_equilateral()}
                """
    def __add__(triangle_a,triangle_b):
        return  str(triangle_a)+str(triangle_b)
    
triangle_a = Triangle(3, 4, 5)
triangle_b = Triangle(5, 5, 6)



# In[ ]:


#Verifying the error for an impossible triangle works
triangle = Triangle(1, 1, 2) #reason this does not work is due to 1+1>2 being wrong


# In[ ]:


# Create an instance of the Circle class

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        return self.radius*pi*2
    
    def area(self):
        return pi*(self.radius**2)
    
    def diameter(self):
        return self.radius*2 
    
    def __str__(self):
            return f"""
                    Perimeter: {circle.perimeter()}
                    Area: {circle.area()}
                    Diameter: {circle.diameter()}
                    """

circle = Circle(5)
print(circle)


# ## Task 4 - Time based while loop (4 points)
# 
# Implement a while loop which runs exactly one minute. 
# 
# You must define a condition and the start time. For this task, orient yourself on the given help in the cells right under this to understand how the ```datetime``` library may be used and how to calculate distances with it.  
# 
# Then, write a starttime and a conditional for the while loop below.

# In[ ]:


datetime.now()


# In[ ]:


starttime = datetime(year=2023, month=5, day=22, hour=12, minute=15, second=0)
print(starttime)


# In[ ]:


endtime= datetime(year=2023, month=5, day=22, hour=13, minute=45, second=0)
print(endtime)


# In[ ]:


distance = endtime - starttime
print(distance)
print(f'The distance between start and end in seconds is equal to {distance.seconds}sec seconds.')
print(f'In minutes this would be {distance.seconds/60}mins, in hours it would be {round(distance.seconds/60/60,2)}h.')




counter = 0
start = #implement start time here

while #implement condition here:
    counter += 1

print(f'Loop started at {start}.')
print(f'Loop ended at approximately {datetime.now()}\n')
print(counter)


# In[ ]:


class time:
    def __init__(t,starttime, endtime):
        t.starttime=starttime
        t.endtime=endtime
        starttime = datetime(year, month, day, hour, minute, second)
        endtime= datetime(year, month, day, hour, minute, second)

    def datetime (t):
        return distance = endtime - starttime

counter = 0
start = input("Enter the starttime")
starttime = datetime(year, month, day, hour, minute, second)
distance = end - start
while distance == (0,0,0,0,1,0):
    counter += 1



# In[ ]:




