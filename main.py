import random
dice_model = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []  # Saves the randomly generated value of dice (integers between 1 and 6)
total = 0  # Initialization of variable total that saves the sum of all the dice values
number_of_dice = int(input("How many dice?: "))  # Input message + value given from keyboard

for die in range(number_of_dice):
    dice.append(random.randint(1, 6))  # Saving the random values of the dice in the dice[] array

for line in range(5):
    for die in dice:
        print(dice_model.get(die)[line], end="")  # Based on the dice_model that we gave, we show every dice
                                                    # from left to right
    print()  # It will display the first line of the first to the last dice, until the last line of the last die

for die in dice:
    total = total + die  # The sum of all the values of the dice
print(f"total: {total}")
