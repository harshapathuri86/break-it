from headers import *
from utility import *

start_time = time.time()
screen_time = time.time()
os.system('clear')

while True:

    time_played = round(time.time()) - round(start_time)
    if((time.time()-screen_time) >= 0.1):
        os.system('clear')
        print_details(time_played)
        display.print_screen()
        screen_time = time.time()
        input()
