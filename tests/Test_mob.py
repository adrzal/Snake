from core.Dice import Dice

dice = Dice()

def show_rolls():
    for x in range(20):
        print(f"{dice.k20(2)}", end="; ")