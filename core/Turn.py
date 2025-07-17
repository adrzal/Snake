# new turn = new object + creator methods as triggers
# 1. read file for Mobs 2. put Mob in [] 3. roll SPD for each
import operator

from core.Dice import Dice


class Turn:
    index = 0
    order = {}

    def __init__(self, dice, mobs):
        Turn.index += 1
        Turn.turn_order(dice, mobs)

    @staticmethod
    def rolling():
        return Dice.k20(1)

    @staticmethod
    def action_sequence(dice, mobs):
        print(f"Turn: {Turn.index}", end=" | ")
        for mob in mobs:
            rolled = dice.k20(1)
            Turn.order.update({mob: rolled})

        for key, value in Turn.order.items():
            #print(f"file: {key}, {value}")
            pass

        order = sorted(Turn.order.items(), key=operator.itemgetter(1), reverse=True)
        print(f"sorted: {order}")
        return order

    @staticmethod
    def turn_order(dice, mobs):
        while True:
            Turn.action_sequence(dice, mobs)

            break
