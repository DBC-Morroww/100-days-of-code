age = input("What is your current age? ")

ninety_minus_age = 90 - int(age)

days = ninety_minus_age * 365
months = ninety_minus_age * 12
weeks = ninety_minus_age * 52

print(f"You have {days} days left until the age ninety. This is {weeks} weeks or {months} months.")
