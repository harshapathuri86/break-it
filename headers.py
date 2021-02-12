from getch import getchar
from alarmexception import AlarmException
import random
import time
import numpy as np
import signal
import os
import sys
from colorama import init, Fore, Back, Style
init()


Screen_height = 41
Screen_width = 160
WIDTH = 400
STARTPOS = 25
INPUT_CHAR = ''
factor = 0
brick_length = 6
brick_height = 2
paddle_step = 6
paddle_sizes = [6, 12, 18]
BRICK0 = " "
BRICK1 = Back.GREEN+" "+Back.RESET
BRICK2 = Back.YELLOW+" "+Back.RESET
BRICK3 = Back.RED+" "+Back.RESET
BRICK4 = Back.BLACK+"-"+Back.RESET
BALLS = []

# PADDLE = Fore.WHITE+"="+Style.RESET_ALL
PADDLE = Back.WHITE+" "+Style.RESET_ALL

# OBJECTS:

BRICKS = [[[BRICK0]*brick_length]*brick_height, [[BRICK1]*brick_length]*brick_height,
          [[BRICK2]*brick_length]*brick_height, [[BRICK3]*brick_length]*brick_height, [[BRICK4]*brick_length]*brick_height]

BALL = [[Fore.RED+"+"+Fore.RESET]]
# BALL = [[Fore.RED+"❐"+Style.RESET_ALL]]
# BALL = [[Fore.WHITE+"·"+Style.RESET_ALL]]

PADDLES = [[[PADDLE]*paddle_sizes[0]]*1,
           [[PADDLE]*paddle_sizes[1]]*1, [[PADDLE]*paddle_sizes[2]]*1]


def view_colours():
    print(Fore.WHITE + Back.LIGHTWHITE_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.MAGENTA + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTCYAN_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTGREEN_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.RED + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTRED_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.LIGHTYELLOW_EX + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
    print(Fore.WHITE + Back.YELLOW + Style.BRIGHT +
          "               ".center(Screen_width)+Style.RESET_ALL)
