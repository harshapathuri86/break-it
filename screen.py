from headers import *


class Screen:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.grid = []

    def create_screen(self):
        self.grid = []
        for i in range(self.__rows):
            self.temp = []
            for j in range(self.__columns):
                self.temp.append(Back.BLACK+" "+Back.RESET)
            self.grid.append(self.temp)

    def print_screen(self):
        for i in range(self.__rows):
            for j in range(self.__columns):
                # print(Back.BLACK + self.grid[i][j] + Back.RESET, end='')
                print(self.grid[i][j], end='')

            print()


display = Screen(Screen_height, Screen_width)
