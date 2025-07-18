from core.units.Unit import Unit


class Player(Unit):
    def __init__(self, collection):
        super().__init__(collection)
        self.is_alive = True