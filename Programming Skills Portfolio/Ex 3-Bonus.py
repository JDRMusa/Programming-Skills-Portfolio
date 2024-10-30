# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:43:25 2024

@author: johnd
"""

print("︵‿︵‿︵‿︵‿︵‿︵‿︵︵‿︵‿︵‿︵‿",
      "\nExercise 3: Advanced Requirements:",
      "\n︵‿︵‿︵‿︵‿︵‿︵‿︵︵‿︵‿︵‿︵‿")

"The requirements is letting the user input their name, hometown, and age instead of setting"
"a fixed value"

#First I need to create a while loop to confirm user inputs, like using a string in an int input
while True:
    try: #The try function checks for errors along the loop
        
        "I created two variables for the name to it can store two inputs"
        Fname= str(input("\nEnter your first Name: "))
        Sname= str(input("\nEnter your second Name: "))
        UHtown = str(input("\nEnter your hometown: "))
        UAge = int(input("\nEnter your age in \033[1mnumbers:\033[0m "))#Bold text is used for emphasis
        break #Breaks the loop if all inputs data types are correctly entered
    except ValueError: #If there is an error in the data that is entered
        print("\n\033[1mInvalid input, please try again.\033[0m")

#Creating a dictionary with the variables containing the user inputs
UserInfo = {'Name' : {Fname,Sname},
            'Hometown' : UHtown,
            'Age' : UAge}

#Printing the info by calling the dictionary
print("\nYour name is",UserInfo['Name'])
print("Your hometown is at:",UserInfo['Hometown'])
print("Your age is:",UserInfo['Age'])