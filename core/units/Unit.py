from core.Dice import Dice


# HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]

class Unit():

    #Mobs_collection = {}
    mobs_array = []

    def __init__(self, collection):
        stats = collection.get('stat')
        self.name = collection.get('name')
        self.HP = collection.get('hit points')
        self.STR = stats.get('STR')
        self.DEX = stats.get('DEX')
        self.CON = stats.get('CON')
        self.INT = stats.get('INT')
        self.WIS = stats.get('WIS')
        self.CHA = stats.get('CHA')
        self.initiative = self.roll_sum(self.DEX)
        Unit.mobs_array.append(self)

    def roll_sum(self, stat):
        return Dice.k20(1) + self.bonus(stat)

    def bonus(self, stat):
        match True:
            case _ if stat >= 20:
                return 5
            case _ if stat >= 18:
                return 4
            case _ if stat >= 16:
                return 3
            case _ if stat >= 14:
                return 2
            case _ if stat >= 12:
                return 1
            case _ if stat >= 10:
                return 0
            case _:
                return -10
