# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:58 2024

@author: johnd
"""

print("\n''''''''''''''''''''''''''''''''''''''''''''''''"
      "\nExercise 8: Simple Search: Optional Requirements"
      "\n,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

"""Allow the user to input the search term instead of using a predefined value and 
implement the search functionality based on user input."""

NameList = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']

x = str.capitalize(input("\nEnter the name of whom would you like to search in the list: "))
if x in NameList:
    print("\n"+x, "is found in the list!")
else:
    print("\n"+x,"is not found in the list!")