import time
from utility import *
from screen import display

start_time = time.time()
screen_time = time.time()
os.system('clear')


while True:

    time_played = round(time.time()) - round(start_time)
    reposition_cursor(0, 0)
    if time.time()-screen_time >= 0.1:
        # os.system('clear')
        display.create_screen()
        screen_time = time.time()
        paddle.display(PADDLES[paddle.gettype()])
        print_details(time_played)
        for brick in bricks:
            brick.checkcollision()
        checkpowerups()
        for pow in powerups:
            pow.activate(paddle)
        for ball in BALLS:
            ball.checkcollision(paddle)

        display.print_screen()
        input_char()
