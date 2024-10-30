# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:55 2024

@author: johnd
"""
"""
Exercise 5: Advanced Requirements:
"""

#Same code as before
print("""\n^^^^^^^^^^^^^^^^^^^^^^^
      \nDays in a Month Counter
      \nvvvvvvvvvvvvvvvvvvvvvvv
      """)
      
Days = {1:"31 days",2:"28 Days",3:" 31 Days",4:"30 Days",
        5:"31 Days",6:"30 Days",7:"31 Days",8:"31 Days",
        9:"30 Days",10:"31 Days",11:"30 Days",12:"31 Days"}

Months = ["January","February","March","April","May","June","July","August","September",
          "October","November","December"]

while True:
    try:
        Selection = int(input("\nEnter the month number you want to check the number of days(Example: 1 = January):"))
        if Selection == 2:# Raises priority in checking February
            year = int(input("\nPlease enter 1 if in normal year or 2 if in leap year:")) 
            #numbers for leap year substitution because it also follow the flow of the exception handler
            if year == 2:# Checks if the year is leap year
                Days.update({2:"29 Days"}) #updates the dictionary to replace 2's value
                print("\nThere are",Days[Selection],"in the month of",Months[Selection-1]+".")
                break
            elif year == 1:# Checks if the year is leap year
                print("\nThere are",Days[Selection],"in the month of",Months[Selection-1]+".")
                break
            else: #If anything else it entered, it will revert back to the first question
                print("\nThe number you entered is invalid, please try again.")
        elif Selection <= 12: #Other argument when any number besides 2 is entered.
            print("\nThere are",Days[Selection],"in the month of",Months[Selection-1]+".")
            break #Important to break while loop
        else: 
            print("\nThe number you entered is invalid, please try again.")
    except ValueError: 
        print("\nPlease enter a number.")
#At this point I should've made a definition that prints ("\nThere are",Days[Selection],"in the month of",Months[Selection-1]+".")