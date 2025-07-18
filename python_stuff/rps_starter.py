from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    comp_move = "rock"
elif num == 2:
    comp_move = "paper"
elif num == 3:
    comp_move = "scissors"

# Ask a user to enter their move
user_move = input("Enter your move (rock, paper, scissors): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("You chose:")
if user_move == "rock":
    print(rock)
elif user_move == "paper":
    print(paper)
elif user_move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Computer chose:")
if comp_move == "rock":
    print(rock)
elif comp_move == "paper":
    print(paper)
elif comp_move == "scissors":
    print(scissors)

# Figure out who wins and print the result!
if comp_move == "rock" and user_move == "scissors":
    print("Computer wins!")
elif comp_move == "scissors" and user_move == "rock":
    print("YOU win!")
elif comp_move == paper and user_move == "rock":
    print("Computer wins!")
elif comp_move == "rock" and user_move == "paper":
    print("YOU win!")
elif comp_move == "scissors" and user_move == "paper":
    print("Computer wins!")
elif comp_move == "paper" and user_move == "scissors":
    print("YOU win!")
elif comp_move == user_move:
    print("It's a tie!")
else:
    print("Invalid move! Please enter rock, paper, or scissors.")