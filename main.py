# ❤️🌲🌊🚁🟩🔥🏥💧🛒☁️🌩️🥇



from pynput import keyboard
from map import Map
import time
import os
import json
from helicopter import Helicopter as Helico
from clouds import Clouds

TICK_SLEEP = .05
TREE_UPDATE = 50
CLOUDS_UPDATE = 65
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_H, MAP_W)
helico = Helico(MAP_W, MAP_H)
tick = 1


#======================================================

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# t - save,  y - load
def process_key(key):
    global helico, tick, clouds, field
    c = key.char.lower()

    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c == 't':
        data = {'helicopter': helico.export_data(), 'clouds': clouds.export_data(), 'field': field.export_data(), 'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'y':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            tick = data['tick'] or 1
            helico.import_data(data['helicopter'])
            field.import_data(data['field'])
            clouds.import_data(data['clouds'])



listener = keyboard.Listener(
    on_press = None,
    on_release = process_key,)
listener.start()





#======================================================

tick = 1
while True:
    os.system('cls')
    field.process_helico(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    tick += 1
    print('TICK', tick)
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.gen_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()