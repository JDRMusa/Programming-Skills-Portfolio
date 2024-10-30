# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:58 2024

@author: johnd
"""

print("\n''''''''''''''''''''''''''''''''''''''''''''''''"
      "\nExercise 8: Simple Search: Optional Requirements"
      "\n,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

#This is a slight variety in the previous one
"""Allow the user to input the search term instead of using a predefined value and 
implement the search functionality based on user input."""

#Same as before, a list
NameList = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']

#This one will always capitalize the first word entered, it helps sort the names as the list is
#also capitalized, it also ask for user input with the message
x = str.capitalize(input("\nEnter the name of whom would you like to search in the list: "))

#Same code as last time, just more fancier
if x in NameList:
    print("\n"+x, "is found in the list!")
#This one has a result if the string is not found.
else:
    print("\n"+x,"is not found in the list!")