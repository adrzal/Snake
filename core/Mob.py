
# HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]

class Mob():

    Mobs_collection = {}

    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE):
        self.name = name
        self.HIT = HIT
        self.DMG = DMG
        self.HP = HP
        self.AC = AC
        self.SPD = SPD
        self.MOVE = MOVE
        Mob.Mobs_collection.update({self.name : [self.name, self.HIT, self.DMG, self.HP, self.AC, self.SPD, self.MOVE]})

    def __eq__(self, Mob):
        print(f"Mob.AC: {Mob.AC}, self.HIT: {self.HIT}, {Mob.AC <= self.HIT}")
        return Mob.AC <= self.HIT


