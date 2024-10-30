# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:57 2024

@author: johnd
"""

print("\n||||||||||||||||||||||||||||||||||||"
      "\nExercise 7: Some Counting - 20 Marks"
      "\n||||||||||||||||||||||||||||||||||||")

"Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case."
#This uses a simple range
print("\n"
      "\nFirst loop: from 0 to 50"
      "\n")

"Write a loop that counts up from 0 to 50 in increments of 1."
#Python starts at 0 so we need to make it stop at 50
for x in range(51):
    if x < 51:
        print(x,end=" ")
        if x == 50:#This will finalize the code
            print("\n"
              "\n||||||||||||||||||||||||||||||||||||"
              "\n|||||||||||1st LOOP END|||||||||||||"
              "\n||||||||||||||||||||||||||||||||||||")

#Separators, you'll see this a lot
print("\n"
      "\nSecond loop: from 50 to 0"
      "\n")

"Write a loop that counts down from 50 to 0 in decrements of 1."
#This one uses parameters, this starts from 51 going to 0
for x in range(51,0,-1):
    if x > 0:
        print(x-1, end=" ")#Since we start at 51, to get 50, we must print out the value -1
        if x == 1:#This will finalize the code using the limit
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||2nd LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")

print("\n"
      "\nThird loop: from 30 to 50"
      "\n")

"Write a loop that counts up from 30 to 50 in increments of 1."
#It follows the same principle as the 2nd but in reverse, in this case, to the positve
for x in range(30,51,1):
    if x < 51:
        print(x, end=" ")
        if x == 50:#This will finalize the code 
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||3rd LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")

print("\n"
      "\nFourth loop: from 30 to 50"
      "\n")

"Write a loop that counts down from 50 to 10 in decrements of 2."
#This one follows 2nd loop in terms of decreasing number, but like 3rd, it has limit
for x in range(50,8,-2):
    if x > 8:#Using 8 allow it to still print the 10
        print(x, end=" ")
        if x == 10:#This will finalize the code, I use 10 so it prints is when it reaches the target
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||4th LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")
            
print("\n"
      "\nFifth loop: from 100 to 200"
      "\n")
            
"Write a loop that counts up from 100 to 200 in increments of 5."
#Final loop that goes by 5
for x in range(100,205,5):
    if x < 205:#Same premise as 4th loop
        print(x, end=" ")
        if x == 200:#This will finalize the code
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||5th LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")