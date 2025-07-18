from core.units.Player import Player


class NPC(Player):
    def __init__(self, name, HIT, DMG, HP, AC, SPD, MOVE):
        super().__init__(name, HIT, DMG, HP, AC, SPD, MOVE)