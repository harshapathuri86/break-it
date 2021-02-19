from colorama import init, Fore, Back, Style

init()

Screen_height = 34
Screen_width = 150
brick_length = 6
brick_height = 2
paddle_step = 6
paddle_sizes = [5, 10, 15]
BRICK0 = " "
BRICK1 = Back.GREEN+" "+Back.RESET
BRICK2 = Back.YELLOW+" "+Back.RESET
BRICK3 = Back.RED+" "+Back.RESET
BRICK4 = Back.BLACK+"-"+Back.RESET
BRICKTYPES = [BRICK0, BRICK1, BRICK2, BRICK3, BRICK4]
PADDLE = Back.WHITE+" "+Style.RESET_ALL

POWERUPS = [[["e"]], [["s"]], [["d"]], [["f"]], [["t"]], [["g"]]]

BRICKS = [[[BRICK0]*brick_length]*brick_height, [[BRICK1]*brick_length]*brick_height,
          [[BRICK2]*brick_length]*brick_height, [[BRICK3]*brick_length]*brick_height, [[BRICK4]*brick_length]*brick_height]

BALL = [[Back.BLACK+ Fore.BLUE+"✱"+Style.RESET_ALL]]

PADDLES = [[[PADDLE]*paddle_sizes[0]]*1,
           [[PADDLE]*paddle_sizes[1]]*1, [[PADDLE]*paddle_sizes[2]]*1]

BALLS = []
bricks = []
powerups = []
newpowerups = []
