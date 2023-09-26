rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
infographics = [rock, paper, scissors]
user_choice = int((input("Do you want to choose rock, paper or scissors? Select 0 for rock, 1 for paper, or 2 for scissors: \n")).lower())

print(f"you selected {infographics[user_choice]}")

# if user_choice == 0:
#     print(rock)
#     print("You selected 'rock'")
# elif user_choice == 1:
#     print(paper)
#     print("You selected 'paper'")
# elif user_choice == 2:
#     print(scissors)
#     print("You selected 'scissors'")

computer_choice = random.randint(0,2)
print(f"Computer selected {infographics[computer_choice]}")
# if computer_choice == 0:
#     print(rock)
#     print("Computer selected 'rock'")
# elif computer_choice == 1:
#     print(paper)
#     print("Computer selected 'paper'")
# elif computer_choice == 2:
#     print(scissors)
#     print("Computer selected 'scissors'")

if computer_choice == 0 and user_choice == 2:
    print("Computer wins, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("Computer wins, you lose!")
elif user_choice == computer_choice:
    print("It's a draw!")