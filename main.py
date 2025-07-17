# TODO: 'Mob' class: constractor with *attributes: HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]   > state as if prone, stunned ect.
# HIT > this vs opponent AC; DMG > damage done on success; HP > heath; AC > armor class; SPD > initiative; MOVE > movement points
# TODO: 'Turn' class: order of actions > main game loop
# TODO: 'Actions' class: actions tokens (Action, Bonus action, Movement, Reaction, Condition, Environmental Effects) > refresh each turn for all mobs
# TODO: 'Dice' class: roll dice like D4, D6, D8, D10, D12, and D20
# TODO: 'Player' class: EQ, stats, spells, abilities, inspiration points, gold, alignment, [**dice modifiers]
# TODO: Save file system > write / read
# TODO: Console for input/output for now > logger
# TODO: save file structure draft [player objects]
# TODO: 1. goblin = Mob(1,2,3..) 2. goblin.createMob() 3. Turn.active[mob list] > append(x) 4. Turn iterate
# TODO: on combat start: 1. add all mobs to set 2. roll SPD for all 3. sort set based on SPD of mob 4. each mob act
# TODO: method to normalize/illiterate inputs for Save class
# TODO: Mob attributes enum legend/key
# TODO: () read file to copy mobs stats to Monsters.json
from core.Dice import Dice
from core.Mob import Mob
from core.Player import Player
from core.Turn import Turn
from utils.Save import Save

mob0 = Player("Eryk", 14, 3, 24, 5, 6, 30)
mob1 = Player("Suzy", 14, 3, 14, 5, 6, 30)
mob2 = Mob("Boblin", 5, 3, 10, 5, 6, 30, 1)

Save.write(mob0, mob1, mob2)

dice = Dice()

for x in Save.read(Save.get_dir()):
    file = Save.read(Save.get_dir()).get(x)
    #print(f"object: {file}; HP: {file.get('HP')}")

for x in range(1):
    turnX = Turn(dice, Save.read(Save.get_dir()))
print("-------------------------------------")
print()

# Unit.Mobs_collection collect every initialized unit
# create mob object based on entity in file > read and assign stats to object while initializing
for x in range(1):
    mobs_dics = Save.read(Save.get_mob_save_dir())
    mob_stats = mobs_dics.get('goblin').get('stat')
    print(f"goblin stats: {mob_stats}")                 # use this
    goblin = Mob("name", mob_stats.get('HIT'), mob_stats.get('HIT'), mob_stats.get('HIT'), mob_stats.get('HIT'), mob_stats.get('HIT'), mob_stats.get('HIT'), mob_stats.get('HIT'),)

