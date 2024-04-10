#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 2
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: String methods, indexing, and slicing.
# 
# ___
# **DEADLINE**: 21st May until 23:59  
# **Your name here**: David Raúl Carranza Navarrete  
# **Your university mail**: dcarranzanav@uni-osnabrueck.de  
# ___
# 
# **Important information**:  
# In order to pass this sheet you need to achieve 10/20 points.  
# For the best possible grade you require 20/20 points, however, since some harder tasks may take a lot of time you don't have to pressure yourself.  
# If you complete any three tasks on a sheet you will definitely get a good grade for that sheet.  
# Hand in your sheet in studip in the respective folder until the deadline.  
# If you receive no email until a few days after the submission deadline you will have passed, the sample solution will also be uploaded around then.  
# If you receive an email you don't need to worry, you can fail one sheet and also your total points will also be taken into account for the final pass or fail.  

# ## Task 1 Multiline printing and number of characters (5 points)
# ### Part 1
# We have learned that there are different ways of printing in multiple lines, using linebreaks for example.  
# Now it is time to write a program that splits the given string into a list of lines.  
# **Hint:** You may need to look up the ```split()``` function, and make sure the variable ```programmer_joke``` is overwritten with the method result.

# In[9]:


programmer_joke = "That\ncode\nlooks\nlike\nit\nis\nsnaking\naround"

programmer_joke=programmer_joke.split()
print(programmer_joke)


# In[3]:


print(x)


# ### Part 2
# By now you are familiar with receiving user input using the ```input()``` function.  
# Write a program that receives two user inputs and stores them in ```string_a``` and ```string_b```.  
# If the first string provided is longer than the second string, print out ```True```, if not, print ```False```.  

# In[19]:


print("Enter string_a")
string_a = int(input())
print("Enter string_b")
string_b = int(input())

if string_a > string_b:
    print("True")
else:
    print("False")


# ## Task 2 If-statements, methods, and strings (4 points)
# Write three conditional statements (filled in for the ```True```), to handle the following four cases.  
# For this you may need to use string methods, you can look at this [link](https://www.w3schools.com/python/python_ref_string.asp).  
# You can find a single method in the list which will solve either conditional, an example is ```char.isalnum()``` which will return True if all letters in ```char``` are alphanumerical.  
# Please handle the following cases for the if-statements in order:
#  1) The char is not an alphanumerical letter.
#  2) The char is a number.
#  3) The char is upper-case.
#  4) The char is lower-case.

# In[89]:


#alternatively you can change the character to check for another value
#char = '+' 

#alternatively you can comment this back in and test for any character
char = input() 


# In[90]:


if not char.isalnum():
    print("The character <", char, "> is not alphanumerical.")

if char == int():
    print("The character <", char, "> is a number.")

elif char.isupper():
    print("The character <", char, "> is an upper case alphabetical.")

elif char.islower():
    print("The character <", char, "> is a lower case alphabetical.")

else:
    print("The character <", char, "> neither of the former options.")


# ## Task 3 Slicing and Indexing (5 points)
# In this task you will receive a list and are asked to change something in it or to access only specific elements of the list.  
# For each cell you will have a ```result``` variable with a print statement right after for checking, make sure you change the value of ```result``` accordingly.  
# 
# 
# Retrieve the ```"Cherry"``` element of the list.

# In[99]:


shopping_list = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]

result = shopping_list[2] #or "Cherry" in shopping_list
print(result)


# Retrieve the first two elements of the list.

# In[97]:


shopping_list = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]
N=2
result = shopping_list[:N]
print(result)


# Retrieve the first two and the last two elements of the list.  
# **HINT:** You may want to use list-addition ```list + list```

# In[105]:


shopping_list = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]
N=2
M=-2

result = shopping_list[:N] + shopping_list[M:]
print(result)


# Retrieve every second item of the list, starting from the Apple.

# In[308]:


shopping_list = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]
N=1
result = shopping_list[N:]
print(result)


# Retrieve the list in reverse.

# In[312]:


shopping_list = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]
result = list(reversed(shopping_list))
print(result)


# Retrieve a list with at least one dairy product, fruit, and sweet, by taking elements from each of the presented lists (don't just make a new list, that will not give you points).  
# **HINT:** You can do this by using the ```[list[idx]]+[list[idx]]+[list[idx]]``` operation.

# In[295]:


import random

shopping_list_fruit = ["Apple", "Banana", "Cherry", "Tomato", "Potato", "Onion"]
shopping_list_dairy = ["Joghurt", "Milk"]
shopping_list_sweets = ["Chocolate", "Popsicle", "Gummy bears"]

l = random.randint(1,6)
m = random.randint(1,2)
n = random.randint(1,3)

result = [shopping_list_fruit[:l]]+[shopping_list_dairy[:m]]+[shopping_list_sweets[:n]]
print(result)


# ## Task 4 Manipulating strings (6 points)
# In this task you are required to manipulate a string ```file_name```  through sequence of actions as follows.   
# Try different file extensions for testing, make sure it works for different file names as well as intended.  

# In[387]:


file_name = "Hello, world.pdf"
file_name = file_name.split()


# Check whether the file contains special characters like colon ":" or coma "," or dollar sign "$", using an if statement.  
# Then, and only if the symbol is in the file name, replace it with an underscore character (```"_"```), using string methods.  

# In[388]:


special_characters=[":",",","$"]
if special_characters in file_name:
    new_file_name = file_name.replace("special_characters","_")


# Finally, check the file type from the extension, and assign the variable ```file_type``` the following values:
# * ```".txt"``` and ```".doc"``` and ```".pdf"``` should output ```"Document file"```
# * ```".jpg"``` and ```".png"``` should output ```"Image file"```
# * ```".mp4"``` and ```".mov"``` should output ```"Video file"```
# * for other types, or if no extension exists, it should print ```"Unsupported file format"```
# 
# **HINT:** For this you may want to take a look at the last three characters of the string in an if statement.

# In[390]:


file_name = "Hello, world.mov"
M=-4
document_file=[".txt",".doc",".pdf"]
image_file=[".jpg",".png"]
video_file=[".mp4", ".mov"]

if file_name[M:] in document_file:
    file_type = "Document file"
    
elif file_name[M:] in image_file:
    file_type = "Image file"
    
elif file_name[M:] in video_file:
    file_type = "Video file"
    
else:
    file_type = "Unsupported file format"

print(file_type)


# In[379]:


print(file_type)


# In[ ]:




