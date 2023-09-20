# User input
print("Welcome to the tip calculator.")
bill = float(input("How much was the total bill? "))
no_of_diners = int(input("How many people are splitting the bill? "))
tip_percent = float(input("Do you want to tip 10, 12, or 15%? "))

# math
tip = bill * (tip_percent / 100)
total_bill = bill + tip
total_bill_pp = int(total_bill) / no_of_diners
final_amount = "{:.2f}".format(total_bill_pp)

# result
print(f"Each person should pay {final_amount}")
