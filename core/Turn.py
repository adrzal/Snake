# new turn = new object + creator methods as triggers
# 1. read file for Mobs 2. put Mob in [] 3. roll SPD for each

class Turn:
    number = 0

    def __init__(self, dice):
        Turn.number += 1
        Turn.turn_order()


    @staticmethod
    def rolling(Dice):
        return Dice.k20(1)

    @staticmethod
    def turn_order():
        while True:
            print(f"Turn: {Turn.number}")
            break
