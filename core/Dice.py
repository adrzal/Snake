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

    @staticmethod
    def k4(quantity):
        return Dice.count(4, quantity)

    @staticmethod
    def k6(quantity):
        return Dice.count(6, quantity)

    @staticmethod
    def k8(quantity):
        return Dice.count(8, quantity)

    @staticmethod
    def k10(quantity):
        return Dice.count(10, quantity)

    @staticmethod
    def k12(quantity):
        return Dice.count(12, quantity)

    @staticmethod
    def k20(quantity):
        return Dice.count(20, quantity)