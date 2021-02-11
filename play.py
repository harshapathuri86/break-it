from headers import *
from utility import *

start_time = time.time()
screen_time = time.time()
os.system('clear')


while True:

    time_played = round(time.time()) - round(start_time)
    if((time.time()-screen_time) >= 0.1):
        os.system('clear')
        display.create_screen()
        screen_time = time.time()
        # ball.setx(random.randint(0, 38))
        # ball.sety(random.randint(6, 156))
        print_bricks()
        print_details(time_played)
        ball.checkcollision(display.grid)
        display.print_screen()
    input()
