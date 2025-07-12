
# HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]

class Mob():
    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE):
        self.name = name
        self.HIT = HIT
        self.DMG = DMG
        self.HP = HP
        self.AC = AC
        self.SPD = SPD
        self.MOVE = MOVE

    def __eq__(self, other, to_compare):
        match to_compare:
            case self.HIT:
                return "Bad request"
            case self.DMG:
                return "Not found"
            case 418:
                return "I'm a teapot"

            case _:
                return "Something's wrong with the internet"

