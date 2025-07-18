from core.units.Unit import Unit


class Mob(Unit):

    index = 0

    def __init__(self, collection):
        super().__init__(collection)
        self.index = Mob.index
        self.is_alive = self.HP > 0
        Mob.index += 1