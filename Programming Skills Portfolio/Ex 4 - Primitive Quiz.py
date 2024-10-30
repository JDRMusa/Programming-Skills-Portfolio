# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:12:36 2024

@author: johnd
"""

print("\nতততততততততততততততততত",
      "\nExercise 4: Primitive Quiz",
      "\nতততততততততততততততততত")

"Step 1: Create a quiz that ask the user for input on 'What is the capital of France?'"
#I created a varuable first for the answer
answer=input("\nWhat is the capital of France?:")

"Step 2: If the answer is correct, the user should receive confirmation that the answer is correct"
#The if function asks if the variable is equal to "Paris"
if answer == "Paris":
    print("Correct Answer!")#This message is displayed when the if requirements is met
#Step 3: If the answer is wrong, the user should receive a message that the answer is wrong
else:
    print("Wrong Answer!")#This message is displayed when the if requirements is not met