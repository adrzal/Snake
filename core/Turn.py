from core.units.Mob import Mob
from core.units.Player import Player
from utils.Save import Save


class Turn:
    index = 0
    order = []
    in_progress = True

    def __init__(self):
        Turn.index += 1
        self.new_round()

    @staticmethod
    def start():
        encounter = Save.read(Save.get_fights_save_dir()).get('encounter_title1')   # read mobs
        mobs_dics = Save.read(Save.get_mob_save_dir())                              # read mobs stats / mapping

        for key in encounter.keys():
            for x in range(encounter.get(key)):
                mob = Mob(mobs_dics.get(key))
                mob.name = key
                Turn.order.append(mob)

        players = Save.read(Save.get_dir())

        for key, value in players.items():
            player = Player(players.get(key))
            player.name = key
            Turn.order.append(player)

        @staticmethod
        def sort_array(unit):
            return unit.initiative

        Turn.order.sort(key=sort_array, reverse=True)

    def new_round(self):
        for x in Turn.order:
            print(f"{x} spd:{x.initiative} HP:{x.HP}, is_alive: {x.is_alive}")
        choose = input().lower()

        if choose == 'k':
            Turn.in_progress = False