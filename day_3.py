# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You are tall enough to ride.")
# else:
#     print("Sorry, you are not tall enough to ride.")


# number = int(input("What number do you want to check? "))

# if number % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight/height ** 2)

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you are normal weight")
# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese")
# else:
#     print(f"Your BMI is {bmi}, you are clinically obese")
    
    
# year = int(input("what year do you want to check?"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"The year {year} is a leap year")
#         else:
#             print(f"The year {year} is not a leap year")
#     else:
#         print(f"The year {year} is a leap year")
# else:
#     print(f"The year {year} is not a leap year")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#     bill += 15
#     if add_pepperoni == "Y":
#         bill += 2
        
# elif size == "M":
#     bill += 20
#     if add_pepperoni == "Y":
#         bill += 3
# else:
#     bill += 25
#     if add_pepperoni == "Y":
#         bill += 3
# if extra_cheese =="Y":
#             bill += 1
# print(f"{bill}")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_names = (name1 + name2).lower()

# t = combined_names.count("t")
# r = combined_names.count("r")
# u = combined_names.count("u")
# e = combined_names.count("e")
# l = combined_names.count("l")
# o = combined_names.count("o")
# v = combined_names.count("v")
# e = combined_names.count("e")

# true = t + r + u + e
# love = l + o + v + e

# love_score = int(str(true) + str(love)) 

# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score > 40 and love_score < 50:
#     print(f"your score is {love_score}, you are alright together")
# else:
#     print(f"your score is {love_score}")


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

option1 = input("Do you want to go left or right? \n").lower()
if option1 == "left":
  option2 = input("You have reached a river at high tide. Do you want to swim across or wait? \n").lower()
  if option2 == "swim":
    option3 = input("You approach three doors, red, white and blue. Which colour door do you want to open? \n").lower()
    if option3 == "red":
      prints("you've entered a room full of fire, game over!")
    elif option3 == "blue":
      print("you've unleashed deadly beasts, game over!")
    elif option3 == "white":
      print('''
                                                        ,jf
   _am,    ,_am,  ,_g_oam,    _am,   _g_ag,   _am,   koewkovg   _mm_
 ,gF  @._-gF   @-"  jf   @  ,gF  @  ^ NX  #_,gF  @     jf      qK  "
 8Y      8Y    d   j#   jF .8Y  ,d   dY     8Y   d    jf       *b,
jK   ,  jK   ,N   jN   jF  :K  ,Z  ,jF     jK  ,Z"  ,jfk,       dN.
 NbpP    NbpP    dP   dFk_o8NbpP"V^dF       NbpY"V^"dF "dYo-"*h,W"
                         ,gF',@'
                        :8K  j8
                         "*w*"

            ''')  
      print("congrats, you've won the challenge")
    else:
      print("game over")
  else:
    print('''
                            e$$$      .c.                  
                          4$$$$     ^$$$$$.
                          $$$$        $$$$$.
                         .$$$$         $$$$$
                      z$$$$$$$$       $$$$$$b
                     $$$$$$""          *$$$$$$.
                     $$$$$                $$$$$r
            \        $$$*     dc    ..    '$$$$b
            4       $$$F      $F    $%     $$$$$       4
            'r     4$$$L  .e$$$$$$$$$$bc    $$$$r      $
             $.    '$$$$z$$$$$$$$$$$$$$$$$..$$$$$     z$
             $$$c   $$$$$$$$$$$$$$$$$$$$$$$$$$$$F  .d$$*
               "$$$. $$$$$$$$$$$$$$$$$$$$$$$$$$P z$$$"
                  "$$b$$$$$$$$$$$$$$$$$$$$$$$$$d$$*
                     "$$$$$$$$$$$$$$$$$$$$$$$$$P"
         ^         .d$$$$$$$$$$$$$$$$$$$$$$$$"
          "e   .e$$$$*"$$$$$$$$$$$$$$$$$$$$$$$$$$e..  e"
           *$$$$P"     ^$$$$$$$$$$$$$$$$$$$$P ""**$$$$
            *"          $$$$$$$$$$$$$$$$$$$P
                      .$$"*$$$$$$$$$$$$P**$$e
                     z$P   J$$$$$$$$$$$e.  "$$c     .
                    d$" .$$$$$$*""""*$$$$$F  "$$. .P
             ^ie.  $$   4$$$"          ^$$     "$$"
                "*$*     "$b           $$"       ^
                           $r          $
                            ".        $     '
                             ^
          ''')
    print("You've been attacked by a swarm of mudcrabs, game over!")
else:
  print("You fell into a hole, game over!")
