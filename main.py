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
from core.Dice import Dice
from core.Mob import Mob
from core.Turn import Turn
from utils.Save import Save

mob0 = Mob("Eryk", 14, 3, 4, 5, 6, 30)
mob1 = Mob("Suzy", 14, 3, 4, 5, 6, 30)
mob2 = Mob("Boblin", 5, 3, 4, 5, 6, 30)

Save.write(mob0, mob1, mob2)

dice = Dice()

turn0 = Turn(dice, Save.read(Save.get_dir()))
turn1 = Turn(dice, Save.read(Save.get_dir()))
turn2 = Turn(dice, Save.read(Save.get_dir()))

