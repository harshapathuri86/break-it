from headers import *


class Object:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x

    def gety(self):
        return self.__x

    def sety(self, x):
        self.__x = x

    def display(self, screen, shape, x, y):
        for i in range(x, x+len(shape)):
            for j in range(y, y+len(shape[0])):
                screen[i][j] = shape[i-x][j-y]


class Brick(Object):

    def __init__(self, x, y, type):
        self.shape = [0]*4
