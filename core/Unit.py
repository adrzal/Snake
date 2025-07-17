
# HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]

class Unit():

    Mobs_collection = {}

    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE):
        self.name = name
        self.HIT = HIT
        self.DMG = DMG
        self.HP = HP
        self.AC = AC
        self.SPD = SPD
        self.MOVE = MOVE
        Unit.Mobs_collection.update({self.name : [self.name, self.HIT, self.DMG, self.HP, self.AC, self.SPD, self.MOVE]})

    def __eq__(self, Unit):
        print(f"Mob.AC: {Unit.AC}, self.HIT: {self.HIT}, {Unit.AC <= self.HIT}")
        return Unit.AC <= self.HIT


