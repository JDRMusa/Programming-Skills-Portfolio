# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:56 2024

@author: johnd
"""
print("""xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Exercise 6: Brute Force Attack
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""") 

"""Basic requirements are: create the password variable, use a loop that enters the correct
   repeatedly asks the user for the right password, and print a confirmation message for the
   right one."""

"Setting the password variable, making it a string type removes any chance of error"
"Even using numbers and symbols"    
setpwd= str("Coding is Cool")

"Using the While True condition to make a simple while loop that is infinite"
while True:
    
    "User input variable with the same data type as the variable"
    enterdpwd= str(input("\nEnter the password (Hint: It's the first exercise): "))
    
    "Condition statement for correct input"
    if enterdpwd == setpwd:
        print("\nPassword is correct, please continue...") #Confirmation message for the right one
        break #Stops the infinite loop
    #If the condition is not met
    else:
        print("\nPassword is incorrect! Please try again...")#Confirmation message that loops the starting code