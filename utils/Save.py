import json
from datetime import datetime

# TODO: save file content / structure

MAIN_SAVE_DIR = "C:\\Users\\Admin\\PycharmProjects\\rpg0.1\\game_save"
MOBS_FILE_DIR = "C:\\Users\\Admin\\PycharmProjects\\rpg0.1\\utils\\Mob_list.json"

class Save:
    now = datetime.now()

    #HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]
    text_data = {
            'Player1': [1, 2, 3, 4, 5],
            'Player2': [],
            'Player3': [],
            'Player4': []
        }


    @staticmethod
    def get_mob_save_dir():
        return MOBS_FILE_DIR

    @staticmethod
    def enter(Mob):
        return {Mob:[Mob.name, Mob.AC, Mob.HP, Mob.DMG, Mob.HIT, Mob.MOVE, Mob.SPD]}


    @staticmethod
    def read():
        pass

    @staticmethod
    def gen_name():
        date_time = Save.now.strftime("%m-%d-%Y %H-%M")
        return f"save{date_time}.json"

    @staticmethod
    def write(Mob):
        Save.text_data.update({f"{Mob.name}": "White"}) # send
        name = Save.gen_name()
        with open(f"{MAIN_SAVE_DIR}\\{name}", 'w', encoding='utf-8') as f:
            json.dump(Save.text_data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def upload_mob(Mob, place):
        Save.text_data.update({f"{Mob.name}": ["Black", "test", "test2"]}) # send
        with open(place, 'w', encoding='utf-8') as f:
            json.dump(Save.text_data, f, ensure_ascii=False, indent=4)