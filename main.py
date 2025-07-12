# TODO: 'Mob' class: constractor with *attributes: HIT; DMG; HP; AC; SPD; MOVE; [**state]; [**actions]   > state as if prone, stunned ect.
# HIT > this vs opponent AC; DMG > damage done on success; HP > heath; AC > armor class; SPD > initiative; MOVE > movement points
# TODO: 'Turn' class: order of actions > main game loop
# TODO: 'Actions' class: actions tokens (Action, Bonus action, Movement, Reaction, Condition, Environmental Effects) > refresh each turn for all mobs
# TODO: 'Dice' class: roll dice like D4, D6, D8, D10, D12, and D20
# TODO: 'Player' class: EQ, stats, spells, abilities, inspiration points, gold, alignment, [**dice modifiers]
# TODO: Save file system > write / read
# TODO: Console for input/output for now > logger
# TODO: save file structure draft [player objects]
from utils.Save import Save

autor = Save()
autor.write()