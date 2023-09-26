# Takes a group of names of diners and selects a party to pay the bill at random, similar to a business card lucky dip.


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
number_of_names = len(names)
random_name = random.randint(0, number_of_names - 1)
print(names[random_name] + " is paying the bill today")