# -*- coding: utf-8 -*-
"""
Don't Learn to Code Until You Master 6 Simple Concepts

Created on Sat Oct 10 11:44:31 2020

@author: Ruby
"""

"""1. Variables"""
#The first variables I showed you were the string, integer and float
gender = "female"
work = "project manager"
age = 31
salary = 39498.75
personality = "good"



"""2. Datatypes"""
#Introducing the boolean and list
is_good = True
shopping_list = ["pizza", "salad", "apples", "cake", "eggs"]

#You can check the datatype like this:
print(type(gender)) 
#This will show the datatype of the gender variable in the console



"""3. Operators"""
#Arithmetic Operators
salary = salary * 0.8
salary_per_month = salary / 12

#Comparison Operators
is_good = personality == "good"
print(is_good)
#This will return true or false based on the condition

#When Ruby looses he job, we update her info
work = "ruby thief"
salary = 0
personality = "evil"

#Try running this again and see what happens
is_good = personality == "good"
print(is_good)



"""4. Functions"""
def make_heist(loot_value) :
    """Function to calculate new salary by adding the loot value
    to the old salary"""
    new_salary = salary + loot_value
    return new_salary

#Functions have an input, process and output
#Once you have a function, you can use it again without writing the code out



"""5. Conditional Statements"""
#Using if else statements:
#Initialise variables
successful = True
loot_value = 1399.99
num_fail = 0

#Calculating Ruby's new salary
if successful :
    salary = make_heist(loot_value) #This is the function we defined earlier
else :
    num_fail = num_fail + 1
#You can see what the salary is now using the print statement:
print(salary)

#Shortcut to adding to or subtracting from variables
num_fail = num_fail + 1
num_fail = num_fail - 1
#The two statements above are equivalent to:
num_fail += 1
num_fail -= 1

#while loops
heist_time = 0

while heist_time <= 60 :
    heist_time += 1 
    #Be careful of infinate loops here
    
    
    
"""Counter for smart-watch app"""
#Initialise status variable
status = "start"

#Count to 60 during heist, then change status to "end"
while status == "start" :
    if heist_time <= 60 :
        heist_time += 1
    else :
        status = "end"
        
#In the statement above the if else statement is nested within the while loop