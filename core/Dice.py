import random

# D4, D6, D8, D10, D12, D20
# TODO: design better dice roller logic
class Dice():

    @staticmethod
    def count(die, quantity):
        result = 0
        for x in range(quantity):
            result += random.randint(1, die)
        return result

    def k4(self, quantity):
        return Dice.count(4, quantity)

    def k6(self, quantity):
        return Dice.count(6, quantity)

    def k8(self, quantity):
        return Dice.count(8, quantity)

    def k10(self, quantity):
        return Dice.count(10, quantity)

    def k12(self, quantity):
        return Dice.count(12, quantity)

    def k20(self, quantity):
        return Dice.count(20, quantity)