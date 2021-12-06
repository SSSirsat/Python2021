import random

active = True
while active:
    message = input("Enter to paly or not (y/n):").lower()
    if message == 'n':
        active = False
    elif message != 'y':
        print("Please enter a valid key")

    else:

        #     def roll_dice():
        you_roll = random.randint(1, 6)
        print(f"your roll is:{you_roll}")
        com_roll = random.randint(1, 6)
        print(f"com roll is:{com_roll}")

        if you_roll < com_roll or com_roll > you_roll:
            print("You loss ")
        else:
            print("You Win")


