"""
Created on Thu Dec 9 11:10:04 2024

@author: johnd
"""
import time
#^Used for creating buffers
import sys, os
#^Used for some defined functions
#Used for table presentation
import pandas as pd
#This is panda options to prevent ellipsis from the table
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
#This is for database, but this also gave me trouble as it is the lite version
import sqlite3
#For flair purposes
title_screen= (r"""
...............................................................................................          
.__            __   _______    ___       _    ________                  _______     _________ .
.\ \          / /  |  _____|  |   \     | |  |  _____ \                /  ____ \   / _______ \.
. \ \        / /   | |        | |\ \    | |  | |     \ \              / /     \ \  | |     |_/. 
.  \ \      / /    | |_____   | | \ \   | |  | |      | |   _______   | |     | |  \ \______  .     
.   \ \    / /     |  _____|  | |  \ \  | |  | |      | |  |_______|  | |     | |   \______ \ .
.    \ \  / /      | |        | |   \ \ | |  | |      | |             | |     | |   _      \ \. 
.     \ \/ /       | |_____   | |    \ \| |  | |_____/ /              \ \_____/ /  / |_____| |.
.      \__/        |_______|  |_|     \___|  |________/                \_______/   \_________/.
...............................................................................................   

      A virtual vending machine.
""")
#To establish the database connection
con=sqlite3.connect("UtilityApp.db",timeout=20,check_same_thread=False)
#To create a cursor in the table of the database
cursor = con.cursor()

#The following are placeholder variables
CurrentMoney = 0.00
Money = 0.00
CurrentTotal = 0.00
multiplier = 0
PriceSelected = 0.00
CurrentStock = 0
itemlist = 0
inv={}
Balance = 0
itemchosen = 0
password = "123"

#The following was used but stopped after it kept giving troubles
#This is used to type out text faster with typewriter effect, used in the title screen
def TypeEffectBigPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.001)
#This is used to type out text with typewriter effect
def TypeEffectPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
#This is used to type out input texts with typewriter effect
def TypeEffectInput(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
   value = input()  
   return value  
#Title Screen
TypeEffectBigPrint(title_screen)
time.sleep(1)

#This is from the previous activities used to insert, update, delete, and show the database
def insertitem(Category,Item,Price,Stock):
    qry="Insert into UtilityApp (Category,Item,Price,Stock) values(?,?,?,?);"
    con.execute(qry,(Category,Item,Price,Stock))
    con.commit()
    print("\nData inserted successfully.")

def updateitem(Category,Item,Price,Number,Stock):
    qry="Update UtilityApp set Category=?,Item=?,Price=?,Stock=? Where Number=?;"
    con.execute(qry,(Category,Item,Price,Number,Stock))
    con.commit()
    print("\nData updated successfully.")
    
def deleteitem(Number):
    qry="Delete from UtilityApp Where Number=?;"
    con.execute(qry,(Number))
    con.commit()
    print("\nData deleted successfully.")
    
def showstocks():
    print (pd.read_sql_query("SELECT * FROM UtilityApp",con))
    TypeEffectPrint("\nStock list found and displayed.")
#Used to select a whole row in the database and display
def chooseitem(number):
    #The global keyword allows the variable to be changed even outside the function
    global itemchosen
    qry="SELECT * FROM UtilityApp Where Number=?;"
    cursor.execute(qry,(number,))
    itemchosen = cursor.fetchall()
    print(itemchosen)
#Fuction for the money sysyem
def moneyin():
    while True:
        try:
            global TotalMoney
            global CurrentMoney
            Money=(float(input('\nInsert Credits:')))
            if type(Money) == float:
                TotalMoney = CurrentMoney + Money
                print('\n',Money,'AED is inserted, Total credits is', TotalMoney)
                CurrentMoney = TotalMoney
                moremoney = input("\n Add more? Enter Y for more or enter any key to go back: ").capitalize()
                if moremoney == "Y":
                    continue
                else:
                    return
            else:
                print('\nInvalid amount, please try again.')
                break
        except ValueError:
            print('\nPlease enter a valid numerical value.')
#This is used for statements that doesn't have the except error handler
def invopt():
    TypeEffectPrint('\nNo valid option was given, please try again...')
    return
#Function that displays the price of the item using the number given
def showprice(number):
    global PriceSelected
    number=number
    qry = "SELECT Price FROM UtilityApp Where Number=?;"
    cursor.execute(qry,(number,))
    PriceSelected = float(''.join(map(str,cursor.fetchone())))
    print(f"\n This item costs {PriceSelected}.")
#This is used to create the total price of the items including ones before the current one
def addcart(multiplier):
    global CurrentTotal
    global PriceSelected
    CurrentTotal = float(CurrentTotal) + float(PriceSelected*multiplier)
    return CurrentTotal
#This is used for listing the dictionary of the purchases and the quantity
def createcart(multiplier,inv):
    global itemlist
    global itemchosen
    itemlist += 1
    for row in itemchosen:
        inv.setdefault(itemlist, []).append({'Item: ': row[2], 
                                             'Price: ': row[3], 
                                             'Quantity: ':multiplier})
#This checks if the current money less than the current total of purchases
def checkout():
    global Balance
    if CurrentMoney < CurrentTotal:
        Balance = round ((CurrentMoney - CurrentTotal), 2)
        print("\nYou don't have enough money to purchase the item.")
        print('Please insert the more credits')
        print(f'\nYou need another {abs(Balance)}AED to buy the item/s.')
        mainmenu()
    else: #This is when the money is enough or more than the total
        Balance = round ((CurrentMoney - CurrentTotal), 2)
        receipt()
#It prints out the table of the dictionary and the remaining change.
def receipt():
    global Balance
    print("Your receipt:")
    Table=pd.DataFrame.from_dict(inv, orient='index')
    print(Table)
    print("\nChange:", Balance)
    print("Have a nice day!")
#This is the whole buying function, it's a bit messy
def buying():
    global CurrentTotal
    while True:
        try:#Choosing the item in the category
            number = int(input("\nChoose an item using the Number: "))
            if type(number) == int:
                chooseitem(number)
                showprice(number)
                multiplier = int(input("\nHow many?: ")) #Creates the quanity
                if type(multiplier) == int:
                    #Makes the variable be operable with the price
                    multiplier=float(multiplier) 
                    #addcart makes it that the total first is displayed
                    addcart(multiplier)
                    #Confirmation
                    print(multiplier,"piece(s) has been selected.")
                    #Shows the current total
                    print(f"\nCurrent total is {CurrentTotal}.")
                    #This confirms the list and creates it
                    createcart(multiplier,inv)
                    #Reconfirmation about continuing
                    finalchoice = input('\nFinish shopping? Y or N: ').capitalize()
                    if finalchoice == "Y":
                        checkout()
                        sys.exit(0)
                    elif finalchoice == "N":
                        mainmenu()
                    else:
                        invopt()
                else:
                    invopt()
            else:
                print('\nInvalid number, please try again.')
                continue
        except ValueError:
            invopt()

mainchoice = "0"

def mainmenu():
    mainchoice = (input("""
          Welcome to the Vending Machine Application.\n 
          The options are simplified for your convenience
          Please choose your desired action by choosing the correct number: 
              
          1. View Items
          2. Insert Credits
          3. Log in
          4. Leave

    """))

    while mainchoice != 4:
        if mainchoice == "1":
            category = (input("""
          Select a category
                  
          1.Drinks
          2.Snacks
          3.Medical
          4.Utility
                  
    Choice: """))
            if category == "1":
                # Like % is used to select data in Category that starts with D 
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'D%'",con)
                # printing a blank space
                print(" ")
                print(cc)
                #Buying code
                buying()
                #Same code with 3 more iterations
            if category == "2":
                # Like % is used to select data in Category that starts with S
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'S%'",con)
                print(" ")
                print(cc)
                buying()
            if category == "3":
                # Like % is used to select data in Category that starts with M
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'M%'",con)
                print(" ")
                print(cc)
                buying()
            if category == "4":
                # Like % is used to select data in Category that starts with U
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'U%'",con)
                print(" ")
                print(cc)
                buying()
            else:
                invopt()
                mainmenu()
        #Choice for the money system
        elif mainchoice == "2":
            moneyin()
            mainmenu()
        #Admin system
        elif mainchoice == "3":
            global password
            #Placeholder password can be changed on the options
            enteredpass=TypeEffectInput("\nEnter the password (Warning: Password is case sensitive): ")
            #Put here as a stopgap for looping problems
            stoploop= "no"
            #There's no limit put for the password
            while enteredpass!=password:
                enteredpass=TypeEffectInput("\nTry again: ")
                if enteredpass==password:
                 break
            #Access granted, options same as last one but with a few addtions
            while enteredpass==password and stoploop=="no": 
                print("""
          1. Insert Item
          2. Update Item
          3. Delete Item
          4. View Stocks
          5. Change Password
          """)
                c=int(input("\nEnter your choice: "))
                try:
                    
                    #Insert now with Stocks
                    if (c == 1):
                        print (
                            """
                            +-----------+
                            |Insert Item|
                            +-----------+
                            """)
                        Category = input("\nEnter your category: ")
                        Item = input("Enter your item: ")
                        Price = float(input("Enter your price: "))
                        Stock = int(input("How many: "))
                        insertitem(Category,Item,Price,Stock)
                
                    #Update now with Stocks
                    elif (c == 2):
                        print (
                            """
                        +-----------+
                        |Update Item|
                        +-----------+
                        """
                        )
                        Number= int(input("Enter the number: "))
                        Category = input("\nEnter your category: ")
                        Item = input("Enter your item: ")
                        Price = float(input("Enter your price: "))
                        Stock = int(input("How many: "))
                        updateitem(Category,Item,Price,Number,Stock)
                        print("\nItem has been updated.")
                
                    #Delete
                    elif (c == 3):
                        print (""""
                               +-----------+
                               |Delete Item|
                               +-----------+
                               """)
                        Number = int(input("\nEnter the number: "))
                        deleteitem(Number)
                
                    #Showing all the table now with Stocks
                    elif (c == 4):
                        TypeEffectPrint("\nShowing stocks.....")
                        showstocks()

                    #Change Password
                    elif (c == 5):
                        password = input("\nInsert the new password: ")
                        TypeEffectPrint("Password is now updated, going back to main menu.")
                        mainmenu()
                        
                    #When the input is invalid
                    else:
                        print("\nInvalid option")
                        enteredpass=(input("\nRe-enter password to continue: "))
                        continue
                    #This gives the user addtional options to do more
                    more=1
                    while more==1:
                        TypeEffectPrint("\nIs there anything else would you like to do?")
                        #Confirmation if for more options
                        confirmation=(input("(Y for yes, N for No): "))
                        confirmation=confirmation.title()
                        if confirmation == "Y" or confirmation == "Yes":
                            TypeEffectPrint("""\nYes confirmed.\n""")
                            break
                        elif confirmation == "N" or confirmation == "No":
                            TypeEffectPrint("""\nNo confirmed.
                            \nThank you for using the Vend-OS, Have a nice day!""")
                            stoploop="yes"
                        #This cleans the console
                            os.system('cls')
                            sys.exit(0)
                            break
                        else:
                            TypeEffectPrint("\nNo valid option was given, please try again...")
                            #Safety measure when mistype
                            more=int(input("\nEnter 1 to continue...: "))
                            if more == 1:
                                continue
                            #Forced system exit after failing the second time
                            else:
                                sys.exit(TypeEffectPrint("No valid option given, good bye. "))
                            break
                except: 
                    print("\nPlease enter a number.")
        #Shutting down feature
        elif mainchoice == "4":
            TypeEffectPrint("Shutting down, thank you for choosing VEND-OS...")
            time.sleep(0.5)
            os.system('cls')
        #This stops the whole program
            sys.exit(0)
        #Return to menu
        else:
            invopt()
            mainmenu()
        break
#Start the program
print(mainmenu())



