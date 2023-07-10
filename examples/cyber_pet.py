from microbit import *
import random

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
Functions to choose a random need, and to check if the pet is happy.
Be careful if you edit these!
'''
def needed():
    needs[random.choice(list(needs.keys()))] = True

def pet_happy():
    return all(value is False for value in needs.values())


'''
A 'dictionary' of things your pet might need help with.
Follow the same format when adding new needs.
'''
needs = {
         'hungry': False,
         'sleepy': False,
         }

while True:
    sleep(100)
    if button_a.was_pressed():
        needed()
    if pet_happy():
        display.show(Image.HEART)

    '''
    What does your pet do when it is hungry or sleepy?
    '''
    if needs['hungry'] is True:
        display.show('H')
    if needs['sleepy'] is True:
        display.show('S')

    '''
    What do you need to do to make your pet happy?
    '''
    if button_b.was_pressed():
        needs['hungry'] = False
    if accelerometer.was_gesture('face down'):
        needs['sleepy'] = False
