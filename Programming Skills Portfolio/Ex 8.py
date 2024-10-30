# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:58 2024

@author: johnd
"""

print("\n'''''''''''''''''''''''''"
      "\nExercise 8: Simple Search"
      "\n,,,,,,,,,,,,,,,,,,,,,,,,,")

"""Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , 
and your task is to search for "Sam"."""

NameList = ['Jake', 'Zac', 'Ian', 'Ron', 'Sam', 'Dave']

print(NameList)

x = 'Sam'
if x in NameList:
    print("I found",x,"!")