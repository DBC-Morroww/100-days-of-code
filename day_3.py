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

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = (name1 + name2).lower()

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")

true = t + r + u + e
love = l + o + v + e

love_score = int(str(true) + str(love)) 

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"your score is {love_score}, you are alright together")
else:
    print(f"your score is {love_score}")
