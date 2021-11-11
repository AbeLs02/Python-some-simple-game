print("WELCOME TO 'ROCK, PAPER, SCISSORS' GAME")

user = str(input("enter your choice(rock, paper or scissors?): "))
if user.lower() not in ["rock", "paper", "scissors"]:
    print("please enter one of the options (rock, paper or scissors)!")
    quit()
else:
    print("user choice: ", user)

import random
computer = ["rock", "paper", "scissors"]
computer_Ran = random.choice(computer)
print("computer choice: ", computer_Ran)

if user == computer_Ran :
    print("There is no winner: *draw*")
elif user == "rock" and computer_Ran == "scissors":
    print("The winner is: *user*.")
elif user == "paper" and computer_Ran == "rock":
    print("The winner is: *user*.")
elif user == "scissors" and computer_Ran == "paper":
    print("The winner is: *user*.")
else:
    print("The winner is: *computer*")



# also we can write codes like:
#
# if (user == "rock" and computer_Ran == "rock") or (user == "paper" and computer_Ran == "paper") or (user == "scissors" and computer_Ran == "scissors"):
#     print("There is no winner: *draw*")
# else:
#     if user == "rock" and computer_Ran == "scissors":
#         print("The winner is: *user*.")
#     else:
#         if user == "paper" and computer_Ran == "rock":
#             print("The winner is: *user*.")
#         else:
#             if user == "scissors" and computer_Ran == "paper":
#                 print("The winner is: *user*.")
#             else:
#                 print("The winner is: *computer*")