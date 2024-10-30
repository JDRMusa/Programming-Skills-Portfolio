# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:56 2024

@author: johnd
"""
print("""xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Exercise 6: Brute Force Attack
------------------------------
Optional Requirements Edition:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""") 

"""Modify the program to include a maximum of 5 password attempts. 
If the user enters the wrong password, inform them of the remaining attempts. 
If the maximum number of attempts is reached, inform the user that the authorities have 
been alerted."""

"First setting the variable"
setpwd= str("Coding is Cool")

"Using the the for loops creates a limit within a certain range of the loop"
for x in range(5):
    
    "User input variable with the same data type as the variable"
    enterdpwd= str(input("\nEnter the password (Hint: It's the first exercise): "))
    
    "Condition statement for correct input"
    if enterdpwd == setpwd:
        print("\n--------------------------------------- \nPassword is correct, please continue...\n---------------------------------------") #Confirmation message for the right one
        break #Stops the for loop
    #If maximum attempts has been made and failed
    elif x == 4:
        print("\n-----------------------------------------------------------------------------------------------"
              "\nPassword is incorrect! Attempts:",x+1,"out of 5. Maximum password attempts has been reached...")
        print("\nThe authorities have been contacted and are now approaching your location, please wait for the eventual termination of your existance. Have a nice day! :)")
        break
    #If the condition is not met"
    else:
        print("\n----------------------------------------------------------------"
              "\nPassword is incorrect! Please try again... Attempts:",x+1,"out of 5."
              "\n----------------------------------------------------------------")#Confirmation message that loops the starting code