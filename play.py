import time
from utility import *
from screen import display

start_time = time.time()
screen_time = time.time()
os.system('clear')


while True:

    time_played = round(time.time()) - round(start_time)
    if time.time()-screen_time >= 0.1:
        os.system('clear')
        display.create_screen()
        screen_time = time.time()
        # ball.setx(random.randint(0, 38))
        # ball.sety(random.randint(6, 156))
        paddle.display(PADDLES[paddle.gettype()])
        print_details(time_played)
        for brick in bricks:
            brick.checkcollision()
        checkpowerups()
        # print(len(BALLS),"BALLS")
        for ball in BALLS:
            ball.checkcollision(paddle)
        display.print_screen()
    input_char()
