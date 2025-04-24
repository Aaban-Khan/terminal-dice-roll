import random 

def game_logic():
    user_input = input(f"Roll the Dice?(y/n): ").lower()
    if user_input == "y":
        dice1 = random.randint(1,6+1)
        dice2 = random.randint(1,6+1)
        print(f"({dice1},{dice2})")
    elif user_input == "n":
        print(f"\nThanks for playing 👏")
    else:
        print(f"\nInvalid choice!")

while True:
    game_logic()
    re_play = input(f"Do you want to Play Again?(y/n): ")
    if re_play != "y":
        print(f"\nThanks for playing 👏")
        break 