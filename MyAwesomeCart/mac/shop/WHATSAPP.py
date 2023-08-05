import random
import pyautogui as pg
import time
animal=('Dog','Cat','Monkey','Buffalow','Elephant','Donkey')
time.sleep(10)
for i in range(15):
    a=random.choice(animal)
    pg.write('you are a ' + a)
    pg.press(enter)