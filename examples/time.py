from microbit import *
from time import ticks_ms

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

'''
get time passed
'''
start_time = ticks_ms()
def check_time():
    current_time = ticks_ms()
    time_passed = current_time - start_time
    return int(time_passed)

'''
main code
'''
hungry = False
while True:
    now = check_time()
    if now > 2000:
        hungry = True
    if hungry == True:
		display.show(Image.SAD)
    else:
		display.show(Image.HAPPY)
    sleep(1000)
