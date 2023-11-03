# ❤️🌲🌊🚁🟩🔥🏥💧🛒☁️🌩️🥇



from pynput import keyboard
from map import Map
import time
import os
from helicopter import Helicopter as Helico


TICK_SLEEP = 2
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
field.gen_forest(5, 10)
field.gen_river(70)
field.gen_river(50)
field.gen_river(12)


helico = Helico(MAP_W, MAP_H)


#======================================================


def process_key(key):
    if key.char == 'a' or key.char == 'A':
        print('Cool')
    
#    if key == keyboard.Key.esc:
#    # Stop listener
#        return False


listener = keyboard.Listener(
    on_press = None,
    on_release = process_key,)
listener.start()





#======================================================

tick = 1
while True:
    os.system('cls')
    print('TICK', tick)
    field. print_map(helico)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.gen_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()