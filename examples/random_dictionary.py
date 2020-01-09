from microbit import *
import random

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

tasks = {
         'hungry': False,
         'sleepy': False,
         }

while True:
    if button_a.was_pressed():
        tasks[random.choice(list(tasks.keys()))] = True

    if all(value is False for value in tasks.values()):
        display.show(Image.HAPPY)

    if tasks['hungry'] is True:
        display.show('H')
    if tasks['sleepy'] is True:
        display.show('S')

    if button_b.was_pressed():
        tasks['hungry'] = False
    if accelerometer.was_gesture('face down'):
        tasks['sleepy'] = False

    sleep(100)
