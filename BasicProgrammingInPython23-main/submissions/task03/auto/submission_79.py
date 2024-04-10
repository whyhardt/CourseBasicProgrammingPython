#!/usr/bin/env python
# coding: utf-8

# # Coding Tasks - Week 3
# Welcome to the Python Programming Exercise Sheet!  
# In this exercise sheet, we will cover some of the fundamental concepts in Python programming.  
# Topics covered are: For- and While-Loops and list methods.
# 
# ___
# **DEADLINE**: 22nd May 12:15  
# **Your name here**: Saru Parajuli
# **Your university mail**: sparajuli@uni-osnabrueck.de
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

# ## Task 1 Looping over strings (4 points)
# 
# Given the string below, print each character of the string and count the number of vowels using a loop structure.  
# Finally, print the number of vowels (AEIOUaeiou) as an output, as stored in the variable ```vowel_count```.  
# **Hint:** You may want to check again what the ```in``` operator in python does for statements like ```'A' in string```.

# In[80]:


my_string = "Summer is coming!"
vowel_count = 0
vowels="aeiouAEIOU"
for char in my_string:
    if char in vowels:
        vowel_count += 1
    print(char)


print("The number of vowels is: ", vowel_count)


# ## Task 2 For and While conversion (6 points)
# For each part you are given an empty list ```result```, and a for or while loop.  
# Convert the for-loops into while-loops and the while-loops into for-loops such that the result will be identical.  
# 
# **Hint:** You may use either ```result += [element]``` or ```result.append(element)``` for the element you wish to add to the ```result``` list.  
# You may find the usage of the condition ```number % 2 == 0``` useful for an if statement in a while loop for the first task.

# ### Part 1 - Even numbers from 2 to 20
# A loop which creates a list of even numbers from 2 to 20.  
# Convert to a while loop.

# In[81]:


result = []
for number in range(2, 21, 2):
    result += [number]
    
print(result)


# In[82]:


result = []
number = 2
while number <= 20:
    if number % 2 == 0:
        result.append(number)
    number +=1

    
print(result)


# ### Part 2 - Snake trivia
# A loop over a list of strings, then add every string which is longer than 8 characters to the ```result``` list.  

# In[83]:


python_text = "The Pythonidae, commonly known as pythons, are a family of nonvenomous snakes found in Africa, Asia, and Australia. Among its members are some of the largest snakes in the world. Ten genera and 39 species are currently recognized. Being naturally non-venomous, pythons must constrict their prey to suffocate it prior to consumption. Pythons will typically strike at and bite their prey of choice to gain hold of it; they then must use physical strength to constrict their prey, by coiling their muscular bodies around the animal, effectively suffocating it before swallowing whole. This is in stark contrast to venomous snakes such as the rattlesnake, for example, which delivers a swift, venomous bite but releases, waiting as the prey succumbs to envenomation before being consumed. Collectively, the pythons are well-documented and -studied as constrictors, much like other non-venomous snakes, including the boas and even kingsnakes of the New World."
python_text = python_text.split(" ")
print(python_text)


# In[84]:


result = []
i = 0

while i < len(python_text):
    if len(python_text[i]) > 8:
        result += [python_text[i]]
    
    i += 1

print(result)


# In[85]:


result = []
for each_word in python_text:
    if len(each_word)> 8:
        result += [each_word]

print(result)


# ## Task 3 List methods (5 points)
# Examine the list methods and find methods suitable for the following four tasks.  
# **Important:** Some methods will alter the object they are called on and some methods may or may not return something. For example, ```string = string.split(",")``` requires the re-assignment to overwrite ```string```, while ```list.remove()``` does not need a re-assignment and will alter the list. For the following methods, test and read so you know which is the case where.

# In[45]:


print(dir(list))


# ### Part 1
# Sort the following list alphabetically from A-Z:

# In[86]:


names = ["Donald Duck", "Minnie Mouse", "Mickey Mouse", "Goofy", "Tick", "Trick", "Track", "Scrooge McDuck", "Daisy Duck", "Pete", "Pluto"]
names.sort()

print(names)


# ### Part 2
# Get the index of "March" in the list and print it:

# In[87]:


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

idx = months.index("March")

print(idx, " is the index of ", months[idx])


# ### Part 3
# Retrieve the last object of the list using the ```pop()``` method and store it in the variable ```removed```.  
# This method removes the last element of a list and alters the list, while also returning it so you can save or use it somewhere.

# In[88]:


alphabet = ["A","B","C","D","E","F","G","H"]

removed = alphabet.pop()

print(removed, " was removed from the alphabet list, which is now: ", alphabet)


# ## Part 4
# Previously we have removed an item from the alphabet list, now we wish to add it back.  
# Add the "H" letter back into the list by inserting it.  
# You may need ```len(alphabet)``` here as argument.

# In[89]:


alphabet = ["A","B","C","D","E","F","G"]
alphabet.insert(len(alphabet),"H")

print(alphabet)


# ### Part 5
# Get the number of occurances of the integer 2 inside this list and print it:

# In[90]:


numbers = [1,2,1,3,2,3,2,1,3,2,2,1,3,2,2,2,1,2,2,3,2,1,3,1,2,3,1,2,3,1,2,3,1,2]

n = numbers.count(2)

print("2 appears ", n, " times in the list.")


# ## Task 4 Restaurant Roulette (5 points)
# 
# Finally it is the weekend!  
# You are going out with some friends to enjoy a nice dinner in Osnabrück.  
# Some of you are really generous that you cannot even decide who is going to pay for the bill.
# 
# In order to tackle this issue, you are going to create a program that will collect all of your names into a list and then selects a random name from that list.  
# Whoever is selected will have to pay for everyone's bill.  
# 
# Implement a while loop that receives inputs, using, for example, ```input("Enter a name or \'stop\', to stop:")``` and stores the input in the list ```names```.  
# Make sure to add a condition to the while loop that will stop the loop, for example checking each iteration if the last input is equal to "stop".  
# Finally, store the selected name in the variable ```selected_name``` and print it.
# 
# **Hint:** For this we imported the ```random``` module, how modules work will be explained in more detail later.  
# For all intents and purposes you can ignore it and simply look at what it does below the loop you implement.

# In[91]:


import random

names = []

while True:
    name= input("Enter a name or 'stop' to stop: ")
    if name == 'stop': 
        break
    names.append(name)

if names:
    selected_name = random.choice(names)

print(selected_name, " will have to pay for everyone's bill.")


# In[ ]:




