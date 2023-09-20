height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round((float(weight)/float(height) ** 2), 2)

print(
    f"Your height is {height}, your weight is {weight}, and your BMI is {bmi}")


# bmi = round(weight/height ** 2)
# if bmi < 18.50:
#     print(f"your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#     print(f"your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#     print(f"your BMI is {bmi}, you are obese.")
# else:
#     print(f"your BMI is {bmi}, you are clinically obese.")
