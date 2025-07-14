# new turn = new object + creator methods as triggers
# 1. read file for Mobs 2. put Mob in [] 3. roll SPD for each
import operator

from core.Dice import Dice


class Turn:
    index = 0
    order = {}

    def __init__(self, dice, mobs):
        Turn.turn_order(dice, mobs)
        Turn.index += 1

    @staticmethod
    def rolling(Dice):
        return Dice.k20(1)

    @staticmethod
    def action_sequance(dice, mobs):
        print("----------------------------")
        print(f"Turn: {Turn.index}", end=" ")
        for mob in mobs:
            rolled = dice.k20(1)
            Turn.order.update({mob: rolled})

        order = sorted(Turn.order.items(), key=operator.itemgetter(1), reverse=True)
        print(f"sorted: {order}")

    @staticmethod
    def turn_order(dice, mobs):
        while True:
            Turn.action_sequance(dice, mobs)

            break
