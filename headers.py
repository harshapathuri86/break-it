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


Screen_height = 40
Screen_width = 170
WIDTH = 400
STARTPOS = 25
INPUT_CHAR = ''
factor = 0

# OBJECTS:
BRICK1 = Fore.LIGHTGREEN_EX+"#"+Fore.RESET
BRICK2 = Fore.LIGHTYELLOW_EX+"#"+Fore.RESET
BRICK3 = Fore.LIGHTRED_EX+"#"+Fore.RESET

COIN = Fore.LIGHTYELLOW_EX + "$"+Fore.RESET
PLUS = Fore.WHITE+Back.CYAN+"+"+Style.RESET_ALL
MAGNET = Fore.LIGHTMAGENTA_EX+"x"+Style.RESET_ALL
ICE1 = Fore.LIGHTCYAN_EX+"("+Fore.RESET
ICE2 = Fore.LIGHTCYAN_EX+"@"+Fore.RESET
ICE3 = Fore.LIGHTCYAN_EX+")"+Fore.RESET


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
