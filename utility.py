import random
import os
from objects import *
from screen import *
from input import *
from headers import *

display = Screen(Screen_height, Screen_width)
display.create_screen()

x = 2
bricks = []
# while x < Screen_height - 8:
while x < Screen_height - 16:
    y = 8
    temp = []
    while y + brick_length <= Screen_width - 4:
        if random.randint(1, 100) <= 80:
            if random.randint(1, 10) <= 9:
                bricks.append(Brick(x, y, random.randint(1, 3)))
                # bricks.append(Brick(x, y, random.randint(1, 1)))
            else:
                bricks.append(Brick(x, y, 4))
        y += brick_length
    x += brick_height
    # bricks.append(temp)


def checkpowerups():
    i = 0
    while i < len(newpowerups):
        if newpowerups[i].check(paddle):
            newpowerups.pop(i)
        else:
            i += 1


def create_objs():
    yp = random.randint(0, Screen_width - paddle_sizes[1])
    yb = random.randint(yp, yp + paddle_sizes[1])
    # ball = Ball(Screen_height-5, yb, -1, 1)
    newball = Ball(Screen_height - 5, yb, -1, 1)
    newpaddle = Paddle(Screen_height - 4, yp, 1)
    newpaddle.sethold(newball)
    BALLS.append(newball)
    powerups.append(expandpaddle())
    powerups.append(shrinkpaddle())
    powerups.append(doubletrouble())
    powerups.append(fastball())
    powerups.append(thruball())
    return newpaddle


paddle = create_objs()


# BALLS.append(Ball(Screen_height-5, 10, -1, 1))


def create_newball():
    yp = paddle.gety()
    yb = random.randint(yp, yp + paddle_sizes[paddle.gettype()])
    # ball = Ball(Screen_height-5, yb, -1, 1)
    ball = Ball(Screen_height - 5, yb, -1, 1)
    paddle.sethold(ball)
    BALLS.append(ball)


def print_details(played_time):
    stat1 = str("  LIVES: " + str(paddle.getlives()) +
                "  |  SCORE:" + str(paddle.getscore()))
    stat2 = str("TIME: " + str(played_time))
    stat3 = str("LEFT : a/h | RIGHT : d/l | QUIT: q")
    lol = Screen_width / 3
    lol = int(lol)
    print(Fore.WHITE + Back.LIGHTRED_EX + Fore.BLACK + Style.BRIGHT +
          stat1.ljust(lol) + stat2.center(lol) + stat3.rjust(lol) + "  " + Style.RESET_ALL)


def input_char():
    char = input_to(Get())
    if char == 'q':
        # os.system('tput reset')
        quit()
    elif char == 'd' or char == 'l':
        t = paddle.gettype()
        y = paddle.gety()
        h = paddle.gethold()
        if y + paddle_sizes[t] + paddle_step <= Screen_width:
            paddle.sety(y + paddle_step)
            if h != 0:
                h.sety(h.gety() + paddle_step)
        else:
            if h != 0:
                if y != (Screen_width - paddle_sizes[t]):
                    h.sety(h.gety() + Screen_width - paddle_sizes[t] - y)
            paddle.sety(Screen_width - paddle_sizes[t])

    elif char == 'a' or char == 'h':
        t = paddle.gettype()
        y = paddle.gety()
        h = paddle.gethold()
        if y - paddle_step >= 0:
            paddle.sety(y - paddle_step)
            if h != 0:
                h.sety(h.gety() - paddle_step)
        else:
            if h != 0:
                if h.gety() != 0:
                    h.sety(h.gety() - y)
            paddle.sety(0)

    elif char == ' ':
        h = paddle.gethold()
        if h != 0:
            paddle.release()
