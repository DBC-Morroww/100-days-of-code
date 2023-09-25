print("Welcome to the rollercoaster ride!")
print("You must be 120cm or taller to ride the rollercoaster.")
height = int(input("How tall are you (cm)?"))
bill = 0

if height >= 120:
    age = int(input("How old are you? "))
    if age >= 18:
        bill += 8
        print("Hop aboard the rollercoaster! One adult ticket will be $12")
    elif age < 18 and age > 12:
        bill += 7
        print("Hop aboard the rollercoaster! One child ticket will be $7")
    else:
        print("Hop aboard the rollercoaster! You may ride for free")

    wants_photo = input("Do you want to have a photo taken? (Y/N)")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you are not tall enough to ride.")