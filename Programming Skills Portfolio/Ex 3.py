# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 21:32:18 2024

@author: johnd
"""

print("""\n>>>>>>>>>>>>>>>>>>>>>
\nExercise 3: Biography
\n<<<<<<<<<<<<<<<<<<<<<""")

"Step 1: Store the name, hometown, and age, like the first exercise, but in a dictionary"
#The UserInfo acts as the dictionary and Name, Hometown, and Age are the key.
#Each key has an appropriate value type
UserInfo = {'Name' : str("John David Musa"),
            'Hometown' : str("Philippines"),
            'Age' : int("24")}

"Step 2: Print the values on separate print() lines"
#Individual print() lines need to have the right variables.
#To call out keys from the dictionary, you must state the dictionart and the key to get the value
print ("\nMy name is",UserInfo['Name'])
print ("I was born in",UserInfo['Hometown'])
print ("I am", UserInfo['Age'], "years old")