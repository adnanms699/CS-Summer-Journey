from random import randint
print("Welcome to the toothpick game!")
print("*" * 25)

player_1 = input("Enter player 1's name: ")
player_2 = input("Enter player 2's name: ")
toothpicks = 15

while True:

    print("|" * toothpicks)
    print(f"There are {toothpicks} toothpicks left in the box. ")
    print(f"How many toothpicks did you take, {player_1}.")
    Picks_taken = int(input("Enter a number between 1 and 3: "))
    toothpicks -= Picks_taken

    if toothpicks <= 0:
        print(f"{player_1} has taken the last toothpick and wins!")
        break

    print("|" * toothpicks)
    print(f"There are {toothpicks} toothpicks left in the box. ")
    print(f"How many toothpicks did you take, {player_2}.")
    Picks_taken = int(input("Enter a number between 1 and 3: "))
    toothpicks -= Picks_taken

    if toothpicks <= 0:
        print(f"{player_1} has taken the last toothpick and wins!")
        break

print("Thanks for playing the toothpick game!")
print("*" * 25)
    




