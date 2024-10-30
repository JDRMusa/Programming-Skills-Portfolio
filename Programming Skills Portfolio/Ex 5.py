# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:50 2024

@author: johnd
"""

"""
Exercise 5: Days of the Month
"""
"The task is to create a program that tells the user how many days are in a specific month."
#This is just for added flair, \n is used to add a nextline = an empty line in the result for spacing
print("""\n=======================
      \nDays in a Month Counter
      \n=======================
      """)
      
"Step 1: Create a dictionary where keys are month in numbers with the value are the number of days."      
#I created a dictionary and a list, Dictionary for the number of days
Days = {1:"31 days",2:"28 Days or 29 Days in leap years",3:" 31 Days",4:"30 Days",
        5:"31 Days",6:"30 Days",7:"31 Days",8:"31 Days",
        9:"30 Days",10:"31 Days",11:"30 Days",12:"31 Days"}
#List for the number of months that will be used in the print section
Months = ["January","February","March","April",
          "May","June","July","August",
          "September","October","November","December"]

"Step 2 and 3: Ask the user for to input a number for the month, and if the input is valid"
"              print the results, if it's invalid, make the user retry."

#While True creates a while loop condition that when the condition is met, it will repeat the function
while True:
#Try is a function that check code if it creates an error.
    try:
        Selection = int(input("\nEnter the month number you want to check the number of days(Example: 1 = January):"))
        if Selection <= 12: #This creates the condition that prints out the result if it's met.
            print("\nThere are",Days[Selection],"in the month of",Months[Selection-1]+".")
            break #This breaks the while Loop
    #Except runs a code if the condition error is met, in this case ValueError is the exception
    except ValueError: 
        print("\nPlease enter a number.") #Printed message when error happens and continue while loop
else: #This continues the while loop when the if statement is false
    print("\nThe number you entered is invalid, please try again.")