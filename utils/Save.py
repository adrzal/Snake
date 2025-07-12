import json
from datetime import datetime

# TODO: save file content / structure

class Save:
    now = datetime.now()

    #HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]
    text_data = {
        'list':
        {
            'Player1': [1, 2, 3, 4, 5],
            'Player2': [],
            'Player3': [],
            'Player4': []
        }
    }

    @staticmethod
    def gen_name():
        date_time = Save.now.strftime("%m-%d-%Y %H-%M")
        return f"save{date_time}.json"

    def write(self):
        name = Save.gen_name()
        with open(f"C:\\Users\\Admin\\PycharmProjects\\rpg0.1\\game_save\\{name}", 'w', encoding='utf-8') as f:
            json.dump(Save.text_data, f, ensure_ascii=False, indent=4)
