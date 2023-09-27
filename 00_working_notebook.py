# DAY 1   

# print("Hello world!")

# print("Hello world!")
# print("Hello world!")
# print("Hello world!")

# print("Hello world!\nHello world!\nHello world!")

# print("Hello" + " world!")
# print('Hello' + ' ' + 'world!')


# print(len(input("What is your name? ")))

# name = input("What is your name? ")
# length = len(name)
# print(length)



# a = input("a: ")
# b = input("b: ")

# c = a
# a = b
# b = c

# print('a = ' + a)
# print('b = ' + b)




# DAY 2

# print("Hello"[4])
# print("Hello"[-1])

# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters")
 
# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

# PEMDAS
# parentheses
# exponentiation
# multiplication
# division
# addition
# subtraction

# L -> R


# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = round((float(weight)/float(height) ** 2), 2)

# # print(int(bmi))
# print(
#     f"Your height is {height}, your weight is {weight}, and your BMI is {bmi}")

# print("Welcome to the rollercoaster ride!")
# print("You must be 120cm or taller to ride the rollercoaster.")
# height = int(input("How tall are you (cm)?"))

# if height >= 120:
#     print("Hop aboard the rollercoaster!")
# else:
#     print("Sorry, you are not tall enough to ride.")

# number = int(input("Which number do you want to check? "))
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# print("Welcome to the rollercoaster ride!")
# print("You must be 120cm or taller to ride the rollercoaster.")
# height = int(input("How tall are you (cm)?"))
# bill = 0

# if height >= 120:
#     age = int(input("How old are you? "))
#     if age >= 18:
#         bill += 8
#         print("Hop aboard the rollercoaster! That will be $8")
#     elif age < 18 and age > 12:
#         bill += 7
#         print("Hop aboard the rollercoaster! That will be $7")
#     else:
#         bill += 6
#         print("Hop aboard the rollercoaster! That will be $6")
    
#     photo = input("Do you want a photo taken? Answer Y or N: ")
#     if photo == "Y":
#         bill += 3
    
#     print(f"your final bill is {bill}")
# else:
#     print("Sorry, you are not tall enough to ride.")


# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")


# print("Welcome to the rollercoaster ride!")
# print("You must be 120cm or taller to ride the rollercoaster.")
# height = int(input("How tall are you (cm)?"))
# bill = 0

# if height >= 120:
#     age = int(input("How old are you? "))
#     if age >= 18:
#         bill += 8
#         print("Hop aboard the rollercoaster! One adult ticket will be $8")
#     elif age < 18 and age > 12:
#         bill += 7
#         print("Hop aboard the rollercoaster! One adult ticket will be $7")
#     else:
#         bill += 6
#         print("Hop aboard the rollercoaster! One adult ticket will be $6")

#     wants_photo = input("Do you want to have a photo taken? (Y/N)")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry, you are not tall enough to ride.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# price = 0

# if size == "S":
#     price += 15
#     if add_pepperoni == "Y":
#         price += 2

# elif size == "M":
#     price += 20
#     if add_pepperoni == "Y":
#         price += 3

# else:
#     price += 25
#     if add_pepperoni == "Y":
#         price += 3

# if extra_cheese == "Y":
#     price += 1

# print(f"Your final bill is ${price}")


# import random
# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")

# import random
# user_input = input("Please select heads or tails: ")
# pc_output = random.randint(0,1)
# if pc_output == 1:
#     print(f"You selected {user_input}, the coin shows Heads")
# else:
#     print(f"You selected {user_input}, the coin shows Tails")	

# states_of_america = ["Delaware", "Pennsylvania", "etc" ]

# states_of_america.append("Texas")

# print(states_of_america)

# states_of_america.extend(["washington", "Nevada"])

# print(states_of_america)

# dirty_dozen = ["strawberries", "spinach", "kale", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "potatoes"]

# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
# vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1])

# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")


# vertical = int(position[0])
# horizontal = int(position[1])

# map[horizontal - 1][vertical - 1] = 'X'

# print(f"{row1}\n{row2}\n{row3}")

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# import random

# user_choice = int((input("Do you want to choose rock, paper or scissors? Select 0 for rock, 1 for paper, or 2 for scissors: \n")).lower())

# if user_choice == 0:
#     print(rock)
#     print("You selected 'rock'")
# elif user_choice == 1:
#     print(paper)
#     print("You selected 'paper'")
# elif user_choice == 2:
#     print(scissors)
#     print("You selected 'scissors'")

# computer_choice = random.randint(0,2)

# if computer_choice == 0:
#     print(rock)
#     print("Computer selected 'rock'")
# elif computer_choice == 1:
#     print(paper)
#     print("Computer selected 'paper'")
# elif computer_choice == 2:
#     print(scissors)
#     print("Computer selected 'scissors'")

# if computer_choice == 0 and user_choice == 2:
#     print("Computer wins, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice > user_choice:
#     print("Computer wins, you lose!")
# elif user_choice == computer_choice:
#     print("It's a draw!")

# fruits = ["apple", "peach", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)    

# student_heights = input("Input a list of student heights seperated by a space ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = 0
# for height in student_heights:
#     total_height += height

# number_of_students = 0
# for height in student_heights:
#     number_of_students += 1
    
# average_height = total_height/number_of_students

# print(f"The average height for this group is {average_height}")


# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score is {highest_score}")


# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
 
# print(total)   

# for number in range(1,101):
#   if number % 15 == 0:
#     number = "Fizzbuzz"
#   elif number % 5 == 0:
#     number = "Buzz"
#   elif number % 3 == 0:
#     number = "Fizz"
#   else:
#     number = number
#   print(number)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level PW generator

# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Advanced Level PW generator

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

