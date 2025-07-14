import json
from datetime import datetime

# TODO: save file content / structure

MAIN_SAVE_DIR = "C:\\Users\\Admin\\PycharmProjects\\rpg0.1\\game_save\\save.json"
MOBS_FILE_DIR = "C:\\Users\\Admin\\PycharmProjects\\rpg0.1\\utils\\Mob_list.json"

class Save:
    now = datetime.now()
    text_data = {}

    @staticmethod
    def get_mob_save_dir():
        return MOBS_FILE_DIR

    @staticmethod
    def get_save_dir():
        return MAIN_SAVE_DIR


    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            data = json.load(file)
        for character in data:
            print(f"{character}:", end=" ")
            for stat in data.get(character):
                print(f"{stat}: {data.get(character).get(stat)}", end=" ")
            print()


    @staticmethod
    def gen_name():
        date_time = Save.now.strftime("%m-%d-%Y %H-%M")
        return f"save{date_time}.json"

    @staticmethod
    def write(*args):
        for x in args:
            # HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]
            Save.text_data.update({f"{x.name}": {'HIT':x.HIT, 'DMG':x.DMG, 'HP':x.HP, 'AC':x.AC, 'SPD':x.SPD, 'MOVE':x.MOVE}}) # send
        with open(MAIN_SAVE_DIR, 'w', encoding='utf-8') as f:
            json.dump(Save.text_data, f, ensure_ascii=False, indent=4)