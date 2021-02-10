from headers import *
import getch
# import classes
# create screen and required items - player, blocks, weapons and powerups
from screen import Screen
display = Screen(Screen_height, Screen_width)
display.create_screen()


def print_details(played_time):
    stat1 = str("  LIVES: "+"lives" + "  |  SCORE:" + "score")
    stat2 = str("TIME: " + str(played_time))
    stat3 = str("QUIT: q")
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
