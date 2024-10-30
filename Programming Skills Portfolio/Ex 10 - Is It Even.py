# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:59 2024

@author: johnd
"""

print("""╭──╯....................╰──╮
┊                          ┊
┊ Exercise 10: Is it even? ┊
┊                          ┊
╰──╮....................╭──╯ """)

"""Write a program that tests if a value is even or odd. Following the instructions 
outlined below:

Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function."""

"First, a function must be created"
#I'm naming my defined function "parity"
def parity ():
    #This creates a placeholder variable that asks for the user input
    a = (input("\nEnter your number (No symbols and letters allowed): "))
    #This function is for checking errors
    try:
        #The line below converts the input into string
        a = int(a)
        if a % 2 == 0:
                print("")#This is an empty line block for neatness
                print((a),"is an even number!")#Resulting an even result message
        else: #If anthing than 0 is the remainder
                print("")
                print (a,"is an odd number!")#Resulting an odd result message
    #This creates a message when anything other than an integer is inputed
    except ValueError:
        print("")
        print (a,"is not a valid number.")

"""
Parity Checker
"""

parity()