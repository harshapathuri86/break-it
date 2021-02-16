from colorama import init, Fore, Back, Style

init()

Screen_height = 40
Screen_width = 150
WIDTH = 400
INPUT_CHAR = ''
brick_length = 6
brick_height = 2
paddle_step = 6
paddle_sizes = [5, 10, 15]
BRICK0 = " "
BRICK1 = Back.GREEN+" "+Back.RESET
BRICK2 = Back.YELLOW+" "+Back.RESET
BRICK3 = Back.RED+" "+Back.RESET
BRICK4 = Back.BLACK+"-"+Back.RESET
BALLS = []
BRICKTYPES = [BRICK0, BRICK1, BRICK2, BRICK3, BRICK4]
# PADDLE = Fore.WHITE+"="+Style.RESET_ALL
PADDLE = Back.WHITE+" "+Style.RESET_ALL

POWERUPS = [[["1"]], [["2"]], [["3"]], [["4"]], [["5"]], [["6"]]]

# OBJECTS:

BRICKS = [[[BRICK0]*brick_length]*brick_height, [[BRICK1]*brick_length]*brick_height,
          [[BRICK2]*brick_length]*brick_height, [[BRICK3]*brick_length]*brick_height, [[BRICK4]*brick_length]*brick_height]

BALL = [[Fore.RED+"+"+Fore.RESET]]
# BALL = [[Fore.RED+"❐"+Style.RESET_ALL]]
# BALL = [[Fore.WHITE+"·"+Style.RESET_ALL]]

PADDLES = [[[PADDLE]*paddle_sizes[0]]*1,
           [[PADDLE]*paddle_sizes[1]]*1, [[PADDLE]*paddle_sizes[2]]*1]


def reposition_cursor(x, y):
    print("\033[%d;%dH" % (x, y))
