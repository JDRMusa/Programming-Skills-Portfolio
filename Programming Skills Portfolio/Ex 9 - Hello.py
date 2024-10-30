# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:58 2024

@author: johnd
"""

print("\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈"
      "\nExercise 9: Hello"
      "\n┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈")

"""Instructions: Fill in the blanks in the code below so that the function hello() 
prints "Hello" to the console."""

#Def creates a customized function that can be ran and repeated along the program
#The task is to fill in the blanks to make a hello function
def hello():
    print("Hello!~")

#Def main() means that it starts the program as the starting point
def main():
    hello()#This is using the hello defined function

#This is assurance control that this main function is still running through the whole program
if __name__ == "__main__":
    main()
    
