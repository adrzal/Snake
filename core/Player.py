from core.Unit import Unit


class Player(Unit):
    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE):
        super().__init__(name, HIT, DMG, HP, AC, SPD, MOVE)