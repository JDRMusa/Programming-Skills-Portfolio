"""
Created on Thu Dec 9 11:10:04 2024

@author: johnd
"""
import time
#^Used for creating buffers
import sys, os
#^Used for some defined functions
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
import sqlite3

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

con=sqlite3.connect("UtilityApp.db",timeout=20,check_same_thread=False)
cursor = con.cursor()
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

def buffer():
    time.sleep(1)
    print()

def TypeEffectBigPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.001)

def TypeEffectPrint(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
      
def TypeEffectInput(text):
   for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.05)
   value = input()  
   return value  

TypeEffectBigPrint(title_screen)
time.sleep(1)

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
    
def chooseitem(number):
    global itemchosen
    qry="SELECT * FROM UtilityApp Where Number=?;"
    cursor.execute(qry,(number,))
    itemchosen = cursor.fetchall()
    print(itemchosen)

def showstocks():
    print (pd.read_sql_query("SELECT * FROM UtilityApp",con))
    TypeEffectPrint("\nStock list found and displayed.")
    
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
                moremoney = input("\n Add more? Y or N: ").capitalize()
                if moremoney == "Y":
                    continue
                else:
                    return
            else:
                print('\nInvalid amount, please try again.')
                break
        except ValueError:
            print('\nPlease enter a valid numerical value.')

def invopt():
    TypeEffectPrint('\nNo valid option was given, please try again...')
    return

def showprice(number):
    global PriceSelected
    number=number
    qry = "SELECT Price FROM UtilityApp Where Number=?;"
    cursor.execute(qry,(number,))
    PriceSelected = float(''.join(map(str,cursor.fetchone())))
    print(f"\n This item costs {PriceSelected}.")
    
def addcart(multiplier):
    global CurrentTotal
    global PriceSelected
    CurrentTotal = float(CurrentTotal) + float(PriceSelected*multiplier)
    return CurrentTotal
    
def createcart(multiplier,inv):
    global itemlist
    global itemchosen
    itemlist += 1
    for row in itemchosen:
        inv.setdefault(itemlist, []).append({'Item: ': row[2], 
                                             'Price: ': row[3], 
                                             'Quantity: ':multiplier})

def checkout():
    global Balance
    if CurrentMoney < CurrentTotal:
        Balance = round ((CurrentMoney - CurrentTotal), 2)
        print("\nYou don't have enough money to purchase the item.")
        print('Please insert the more credits')
        print(f'You need another {abs(Balance)}AED to buy the item/s.')
        mainmenu()
    else:
        Balance = round ((CurrentMoney - CurrentTotal), 2)
        receipt()
        
def receipt():
    global Balance
    global itemchosen
    print("Your receipt:")
    Table=pd.DataFrame.from_dict(inv, orient='index')
    print(Table)
    print("\nChange:", Balance)
    print("Have a nice day!")


def buying():
    global CurrentTotal
    while True:
        try:
            number = int(input("\nChoose an item using the Number: "))
            if type(number) == int:
                chooseitem(number)
                showprice(number)
                multiplier = int(input("\nHow many?: "))
                if type(multiplier) == int:
                    multiplier=float(multiplier)
                    addcart(multiplier)
                    print(multiplier,"piece(s) has been selected.")
                    print(f"\nCurrent total is {CurrentTotal}.")
                    createcart(multiplier,inv)
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
                # printing the cursor data
                print(" ")
                print(cc)
                buy = input('\nBuy something? Y for yes and N for no, remember to put credits: ').capitalize()
                if buy == "Y": 
                    buying()
                elif buy == "N":
                    mainmenu()
                else:
                    invopt()
                    continue
            if category == "2":
                # Like % is used to select data in Category that starts with D 
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'S%'",con)
                # printing the cursor data
                print(" ")
                print(cc)
                buy = input('\nBuy something? Y for yes and N for no, remember to put credits:').capitalize()
                if buy == "Y": 
                    buying()
                elif buy == "N":
                    mainmenu()
                else:
                    invopt()
                    continue
            if category == "3":
                # Like % is used to select data in Category that starts with D 
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'M%'",con)
                # printing the cursor data
                print(" ")
                print(cc)
                buy = input('\nBuy something? Y for yes and N for no, remember to put credits:').capitalize()
                if buy == "Y": 
                    buying()
                elif buy == "N":
                    mainmenu()
                else:
                    invopt()
                    continue
            if category == "4":
                # Like % is used to select data in Category that starts with D 
                cc = pd.read_sql_query("SELECT * from UtilityApp WHERE Category Like'U%'",con)
                # printing the cursor data
                print(" ")
                print(cc)
                buy = input('\nBuy something? Y for yes and N for no, remember to put credits:').capitalize()
                if buy == "Y": 
                    buying()
                elif buy == "N":
                    mainmenu()
                else:
                    invopt()
                    continue
            else:
                invopt()
                mainmenu()
        elif mainchoice == "2":
            moneyin()
            mainmenu()
        elif mainchoice == "3":
            enteredpass="a"
            enteredpass=TypeEffectInput("Enter the password (Warning: Password is case sensitive): ")
            password= "a"
            while enteredpass!=password:
                enteredpass=TypeEffectInput("\nTry again: ")
                if enteredpass==password:
                 break
            while enteredpass==password: 
                print("""
                  1. Insert Item
                  2. Update Item
                  3. Delete Item
                  4. View Stocks
                  5. Change Password
                  """)
                c=int(input("\nEnter your choice: "))
                try:
                #Insert
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
                
                    #Update
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
                
                    #Showing all the table
                    elif (c == 4):
                        TypeEffectPrint("\nShowing stocks.....")
                        showstocks()
                    #Change Password
                    elif (c == 5):
                        password = input("\nInsert the new password: ")
                    #When the input is invalid
                    else:
                        print("\nInvalid option")
                        password=(input("\nRe-enter password to continue: "))
                        continue
                    #This gives the user addtional options to do more
                    
                    more=1
                    while more==1:
                        TypeEffectPrint("\nIs there anything else would you like to do?")
                        confirmation=(input("(Y for yes, N for No): "))
                        confirmation=confirmation.title()
                        if confirmation == "Y" or confirmation == "Yes":
                            TypeEffectPrint("""\nYes confirmed.\n""")
                            break
                        elif confirmation == "N" or confirmation == "No":
                            TypeEffectPrint("""\nNo confirmed.
                            \nThank you for using the Vend-OS, Have a nice day!""")
                            break
                        else:
                            TypeEffectPrint("\nNo valid option was given, please try again...")
                            more=int(input("\nEnter 1 to continue...: "))
                            if more == 1:
                                continue
                            else:
                                sys.exit(TypeEffectPrint("No valid option given, good bye. "))
                    continue
                    break
                except ValueError: 
                    print("\nPlease enter a number.")
        elif mainchoice == "4":
            TypeEffectPrint("Shutting down, thank you for choosing VEND-OS...")
            time.sleep(0.5)
            os.system('cls')
            sys.exit(0)
        else:
            invopt()
            mainmenu()
        break

print(mainmenu())



