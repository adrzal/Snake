from core.Unit import Unit


class Mob(Unit):
    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE, CR):
        super().__init__(name, HIT, DMG, HP, AC, SPD, MOVE)
        self.CR = CR

    drop_table = ["gold", "sword", "bow"]