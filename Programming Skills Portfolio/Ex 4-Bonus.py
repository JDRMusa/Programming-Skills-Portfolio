# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:20:57 2024

@author: johnd
"""

print("\n●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●",
      "\nExercise 4: Primitive Quiz, Advanced Edition!",
      "\n●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●")

print("\nWelcome to the \033[1mWHAT'S THE BIG C\033[0m, where you guess what is the capital of the city!")
#First create 10 variables with the correct answers
Questions=[("What is the captial of \033[1mFrance\033[0m? (It should be obvious)","Paris"),
           ("What is the captial of \033[1mLuxembourg\033[0m? (Hint: It\'s in there )","Luxembourg City"),
           ("What is the captial of \033[1mSwitzerland\033[0m (Hint: Deja vu?)","Switzerland"),
           ("This one should be a little bit hard, what is the capital of \033[1mLatvia\033[0m","Riga"),
           ("The country is known for some, but what is the capital of \033[1mFinland\033[0m","Helsinki"),
           ("On the contrary to common belief, \033[1mPortugal\033[0m is a country, what is it's capital","Lisbon"),
           ("A place with a nice view! \033[1mBulgaria\033[0m's capital is","Sofia"),
           ("The land of the luck and leprachaun, what is the capital of \033[1mIreland\033[0m","Dublin"),
           ("You can see the country of \033[1mGeorgia\033[0m on some flight ads, what is the capital","Tbilisi"),
           ("\033[1mIceland\033[0m is really green in contrast of it's name, what is the capital","Reykjavik")]
score = 0

for question, capital in Questions:
    answer = input(f"\n{question}: ").title()
    
    if answer == capital:
        print("Correct, keep that going! On to the next one!")
        score = score + 1
    else:
        print(f"Oooh, Sorry...The answer is {capital!r}, and not {answer!r}. On to the next question!")

if score < 5:
    print("\nYou've scored",score,"out of 10, better luck next time!")
elif score == 0:
    print("\nOooof, you better study hard! You got",score,"out of 10. Don't slack off!")
elif score == 10:
    print("\n\033WOW\033[0m You got a perfect score!",score,"out of 10")
else:
    print("\nCongratulations! You got",score,"out of 10, that's way more than half!")