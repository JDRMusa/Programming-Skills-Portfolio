# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:57 2024

@author: johnd
"""

print("\n||||||||||||||||||||||||||||||||||||"
      "\nExercise 7: Some Counting - 20 Marks"
      "\n||||||||||||||||||||||||||||||||||||")

"Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case."
#
print("\n"
      "\nFirst loop: from 0 to 50"
      "\n")

"Write a loop that counts up from 0 to 50 in increments of 1."
#
for x in range(51):
    if x < 51:
        print(x,end=" ")
        if x == 50:
            print("\n"
              "\n||||||||||||||||||||||||||||||||||||"
              "\n|||||||||||1st LOOP END|||||||||||||"
              "\n||||||||||||||||||||||||||||||||||||")

print("\n"
      "\nSecond loop: from 50 to 0"
      "\n")

"Write a loop that counts down from 50 to 0 in decrements of 1."
#
for x in range(51,0,-1):
    if x > 0:
        print(x-1, end=" ")
        if x == 1:
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||2nd LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")

print("\n"
      "\nThird loop: from 30 to 50"
      "\n")

"Write a loop that counts up from 30 to 50 in increments of 1."
#
for x in range(30,51,1):
    if x < 51:
        print(x, end=" ")
        if x == 50:
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||3rd LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")

print("\n"
      "\nFourth loop: from 30 to 50"
      "\n")

"Write a loop that counts down from 50 to 10 in decrements of 2."
#
for x in range(50,8,-2):
    if x > 8:
        print(x, end=" ")
        if x == 10:
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||4th LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")
            
print("\n"
      "\nFifth loop: from 100 to 200"
      "\n")
            
"Write a loop that counts up from 100 to 200 in increments of 5."
#
for x in range(100,205,5):
    if x < 205:
        print(x, end=" ")
        if x == 200:
            print("\n"
                  "\n||||||||||||||||||||||||||||||||||||"
                  "\n|||||||||||5th LOOP END|||||||||||||"
                  "\n||||||||||||||||||||||||||||||||||||")