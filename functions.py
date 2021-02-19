from objects import *
from input import *
from headers import *


def checkpowerups():
    i = 0
    while i < len(newpowerups):
        if newpowerups[i].check(paddle):
            newpowerups.pop(i)
        else:
            i += 1


def create_objs():
    x = 4
    while x < Screen_height - 16:
        y = 6
        temp = []
        while y + brick_length <= Screen_width - 6:
            if random.randint(1, 100) <= 80:
                if random.randint(1, 10) <= 9:
                    bricks.append(Brick(x, y, random.randint(1, 3)))
                else:
                    bricks.append(Brick(x, y, 4))
            y += brick_length
        x += brick_height
    yp = random.randint(0, Screen_width - paddle_sizes[1])
    yb = random.randint(yp, yp + paddle_sizes[1])
    newball = Ball(Screen_height - 5, yb, -1, 1)
    newpaddle = Paddle(Screen_height - 4, yp, 1)
    newpaddle.sethold(newball)
    BALLS.append(newball)
    powerups.append(expandpaddle())
    powerups.append(shrinkpaddle())
    powerups.append(doubletrouble())
    powerups.append(fastball())
    powerups.append(thruball())
    powerups.append(paddlegrab())
    return newpaddle


paddle = create_objs()


def print_details(played_time):
    stat1 = str("  LIVES: " + str(paddle.getlives()) +
                "  |  SCORE:" + str(paddle.getscore()))
    stat2 = str("TIME: " + str(played_time))
    stat3 = str("LEFT : A | RIGHT : D | QUIT: Q ")
    lol = Screen_width / 3
    lol = int(lol)
    print(Fore.WHITE + Back.LIGHTRED_EX + Fore.BLACK + Style.BRIGHT +
          stat1.ljust(lol) + stat2.center(lol) + stat3.rjust(lol) + Style.RESET_ALL)


def input_char():
    char = input_to(Get())
    if char == 'q' or char == 'Q':
        os.system('tput reset')
        quit()
    elif char == 'd' or char == 'D':
        paddle.moveright()
    elif char == 'a' or char == 'A':
        paddle.moveleft()
    elif char == ' ':
        if len(paddle.gethold()) > 0:
            paddle.release()
