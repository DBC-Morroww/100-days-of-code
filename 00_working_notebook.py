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

states_of_america = ["Delaware", "Pennsylvania", "etc" ]

states_of_america.append("Texas")

print(states_of_america)

states_of_america.extend(["washington", "Nevada"])

print(states_of_america)