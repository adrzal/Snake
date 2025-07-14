import json
from datetime import datetime
import Config

class Save:
    now = datetime.now()
    text_data = {}

    @staticmethod
    def get_mob_save_dir():
        return Config.MOBS_FILE_DIR

    @staticmethod
    def get_dir():
        return Config.MAIN_SAVE_DIR


    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            data = json.load(file)
        for character in data:
            print(f"{character}:", end=" ")
            for stat in data.get(character):
                print(f"{stat}: {data.get(character).get(stat)}", end=" ")
            print()
            return data


    @staticmethod
    def gen_name():
        date_time = Save.now.strftime("%m-%d-%Y %H-%M")
        return f"save{date_time}.json"

    @staticmethod
    def write(*args):
        for x in args:
            Save.text_data.update({f"{x.name}": {'HIT':x.HIT, 'DMG':x.DMG, 'HP':x.HP, 'AC':x.AC, 'SPD':x.SPD, 'MOVE':x.MOVE}})
        with open(Config.MAIN_SAVE_DIR, 'w', encoding='utf-8') as f:
            json.dump(Save.text_data, f, ensure_ascii=False, indent=4)