class Player():
    """
    Any object on the screen    
    """

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
