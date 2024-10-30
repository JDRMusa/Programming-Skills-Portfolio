# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:58 2024

@author: johnd
"""
print("\n'''''''''''''''''''''''''"
      "\nExercise 8: Simple Search"
      "\n,,,,,,,,,,,,,,,,,,,,,,,,,")

#Doing a very simple search program in the console
"""Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
and your task is to search for "Sam"."""

#A NameList list for the list of names containing the names that needs to be listed
NameList = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']

#Printing the list for proof
print(NameList)

#The actual program
x = 'Sam'#The variable x is containing the value of 'Sam'
#An if statement utilizing in, the function that searches the value before the in is stated.
if x in NameList:
    #if the statement is true
    print("I found",x,"!")
