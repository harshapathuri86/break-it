import time
from functions import *
from screen import display

start_time = time.time()
screen_time = time.time()
os.system('clear')


while True:

    print("\033[%d;%dH" % (0, 0))
    time_played = round(time.time()) - round(start_time)
    if time.time()-screen_time >= 0.1:
        display.create_screen()
        screen_time = time.time()
        paddle.display(PADDLES[paddle.gettype()])
        print_details(time_played)
        for brick in bricks:
            brick.checkcollision()
        checkpowerups()
        for power in powerups:
            power.activate(paddle)
        for ball in BALLS:
            ball.checkcollision(paddle)

        display.print_screen()
        input_char()
