# A simple choose your own adventure game, using ascii art and nested if/elifs

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
  
  

