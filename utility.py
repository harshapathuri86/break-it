from headers import *
import getch
from objects import *
# import classes
# create screen and required items - player, blocks, weapons and powerups
from screen import Screen

display = Screen(Screen_height, Screen_width)
display.create_screen()

x = 2
bricks = []
while x < Screen_height - 8:
    y = 8
    temp = []
    while y+brick_length <= Screen_width - 4:
        if random.randint(1, 100) <= 80:
            if random.randint(1, 10) <= 9:
                bricks.append(Brick(x, y, random.randint(1, 3)))
            else:
                bricks.append(Brick(x, y, 4))
        y += brick_length
    x += brick_height
    # bricks.append(temp)


ball = Ball(10, 0, -1, 1)
# ball.display(display.grid, BALL)
paddle = Paddle(50, 1)


def print_ball():
    # fx = ball.getx()+ball.x_v
    # fy = ball.gety()+ball.x_y

    ball.setx(ball.getx()+ball.getxv())
    ball.sety(ball.gety()+ball.getyv())
    ball.display(display.grid, BALL)


def print_bricks():
    grid = display.grid
    paddle.display(grid, PADDLES[paddle.gettype()])
    for a in bricks:
        a.display(grid, BRICKS[a.gettype()])

    type, x, y = ball.getbt()
    if type == 0:
        return
    for a in bricks:
        if a.gettype() != type or a.gettype() == 4:
            continue
        bx = a.getx()
        by = a.gety()
        if (x-bx) < brick_height and (y-by) < brick_length:
            a.settype(type-1)
            return
        # # check collision after bricks are printed
        # # need to do collision diagonally
        # for i in range(brick_length):
        #     if grid[bx-1][by+i] == BALL or grid[bx+brick_height][by+i] == BALL:
        #         a.settype(type-1)
        #         return
        # for i in range(brick_height):
        #     if grid[bx+i][by-1] == BALL or grid[bx+i][by+brick_length] == BALL:
        #         a.settype(type-1)
        #         return


def print_details(played_time):
    stat1 = str("  LIVES: "+"lives" + "  |  SCORE:" + "score")
    stat2 = str("TIME: " + str(played_time))
    stat3 = str("LEFT : a/h | RIGHT : d/l | QUIT: q")
    lol = Screen_width/3
    lol = int(lol)
    print(Fore.WHITE + Back.LIGHTRED_EX + Fore.BLACK + Style.BRIGHT +
          stat1.ljust(lol)+stat2.center(lol)+stat3.rjust(lol)+"  "+Style.RESET_ALL)


def input():
    def alarmhandler(signum, frame):
        raise AlarmException

    def user_input(timeout=0.1):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getchar()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''
    INPUT_CHAR = user_input()
    char = INPUT_CHAR

    if char == 'q':
        os.system('tput reset')
        quit()
    elif char == 'd' or char == 'l':
        t = paddle.gettype()
        y = paddle.gety()
        if y+paddle_sizes[t] + paddle_step <= Screen_width:
            paddle.sety(y+paddle_step)
        else:
            paddle.sety(Screen_width-paddle_sizes[t])
    elif char == 'a' or char == 'h':
        t = paddle.gettype()
        y = paddle.gety()
        if y - paddle_step >= 0:
            paddle.sety(y-paddle_step)
        else:
            paddle.sety(0)
