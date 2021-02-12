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
        return self.__y

    def sety(self, y):
        self.__y = y

    def display(self, screen, shape):
        for i in range(self.__x, self.__x+len(shape)):
            for j in range(self.__y, self.__y+len(shape[0])):
                try:
                    screen[i][j] = shape[i-self.__x][j-self.__y]
                except:
                    print("ERR")
                    print(i, j, self.__x, self.__y)
                    quit()

    # def display(self, screen, shape, x, y):
    #     for i in range(x, x+len(shape)):
    #         for j in range(y, y+len(shape[0])):
    #             screen[i][j] = shape[i-x][j-y]


class Brick(Object):

    def __init__(self, x, y, type):
        self.__type = type
        Object.__init__(self, x, y)

    def gettype(self):
        return self.__type

    def settype(self, type):
        self.__type = type


class Ball(Object):
    def __init__(self, x, y, x_velocity, y_velocity):
        self.__x_v = x_velocity
        self.__y_v = y_velocity
        self.__collided_brick_type = 0
        self.__collided_brick_x = 0
        self.__collided_brick_y = 0
        self.__onhold = True
        Object.__init__(self, x, y)

    def setxv(self, x_velocity):
        self.__x_v = x_velocity

    def getxv(self):
        return self.__x_v

    def getbt(self):
        return self.__collided_brick_type, self.__collided_brick_x, self.__collided_brick_y

    def getcb(self):
        return self.__collided_dia

    def sethold(self, value):
        self.__onhold = value

    def gethold(self):
        return self.__onhold

    def setyv(self, y_velocity):
        self.__y_v = y_velocity

    def getyv(self):
        return self.__y_v

    def checkcollision(self, grid, paddle):
        if self.__onhold:
            self.display(grid, BALL)
            return
        # self.setx(self.getx()+self.getxv())
        # self.sety(self.gety()+self.getyv())
        self.__collided_brick_type = 0
        # self.display(grid, BALL)
        bx = self.getx()+self.getxv()
        by = self.gety()+self.getyv()
        xv = -1
        yv = -1
        check = False
        if self.getxv() > 0:
            xv = 1
        if self.getyv() > 0:
            yv = 1
        # borders of screen
        if bx >= Screen_height-1:
            self.setx(Screen_height-1)
            self.setxv(-self.getxv())
            ### OUT ###
            paddle.declives()
            # need to place the ball randomly on paddle if no balls are present else delete ball
            return
        elif bx <= 0:
            self.setx(0)
            self.setxv(-self.getxv())
            check = True
        if by >= Screen_width-1:
            self.sety(Screen_width)
            self.setyv(-self.getyv())
            check = True
        elif by <= 0:
            self.sety(0)
            self.setyv(-self.getyv())
            check = True
        if not check:
            c1 = False
            c2 = False
            c3 = False
            type = 0
            if grid[bx+xv][by] == BRICK1:
                c1 = True
                self.__collided_brick_type = 1
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by
            if grid[bx+xv][by] == BRICK2:
                c1 = True
                self.__collided_brick_type = 2
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by

            if grid[bx+xv][by] == BRICK3:
                c1 = True
                self.__collided_brick_type = 3
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by

            if grid[bx+xv][by] == BRICK4:
                c1 = True
                self.__collided_brick_type = 4
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by
            if grid[bx][by+yv] == BRICK1:
                c2 = True
                self.__collided_brick_type = 1
                self.__collided_brick_x = bx
                self.__collided_brick_y = by+yv
            if grid[bx][by + yv] == BRICK2:
                c2 = True
                self.__collided_brick_type = 2
                self.__collided_brick_x = bx
                self.__collided_brick_y = by+yv
            if grid[bx][by+yv] == BRICK3:
                c2 = True
                self.__collided_brick_type = 3
                self.__collided_brick_x = bx
                self.__collided_brick_y = by+yv
            if grid[bx][by+yv] == BRICK4:
                c2 = True
                self.__collided_brick_type = 4
                self.__collided_brick_x = bx
                self.__collided_brick_y = by+yv
            if grid[bx+xv][by+yv] == BRICK1:
                c3 = True
                self.__collided_brick_type = 1
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by+yv
            if grid[bx+xv][by + yv] == BRICK2:
                c3 = True
                self.__collided_brick_type = 2
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by+yv
            if grid[bx+xv][by+yv] == BRICK3:
                c3 = True
                self.__collided_brick_type = 3
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by+yv
            if grid[bx+xv][by+yv] == BRICK4:
                c3 = True
                self.__collided_brick_type = 4
                self.__collided_brick_x = bx+xv
                self.__collided_brick_y = by+yv
            # if grid[bx+xv][by] == BRICK1 or grid[bx+xv][by] == BRICK2 or grid[bx + xv][by] == BRICK3 or grid[bx+xv][by] == BRICK4:
            #     c1 = True
            # if grid[bx][by+yv] == BRICK1 or grid[bx][by + yv] == BRICK2 or grid[bx][by+yv] == BRICK3 or grid[bx][by+yv] == BRICK4:
            #     c2 = True
            # if grid[bx+xv][by+yv] == BRICK1 or grid[bx+xv][by + yv] == BRICK2 or grid[bx+xv][by+yv] == BRICK3 or grid[bx+xv][by+yv] == BRICK4:
            #     c3 = True
            if self.__collided_brick_type != 0:
                paddle.addscore(self.__collided_brick_type)
            if c1:
                self.setxv(-self.getxv())
            if c2:
                self.setyv(-self.getyv())
            if not c1 and not c2 and c3:
                self.setxv(-self.getxv())
                self.setyv(-self.getyv())
        self.setx(bx)
        self.sety(by)
        self.display(grid, BALL)


class Paddle(Object):
    def __init__(self, x, y, type):
        self.__type = type  # powerup
        self.__lives = 3
        self.__score = 0
        self.__powerup = 0
        self.__onhold = 0
        Object.__init__(self, x, y)

    def settype(self, type):
        self.__type = type

    def gettype(self):
        return self.__type

    def addscore(self, add):
        if add == 1:
            self.__score += 10
        elif add == 2:
            self.__score += 15
        elif add == 3:
            self.__score += 20
        # elif add == 4:

    def setpowerup(self, powerup):
        self.__powerup = powerup

    def getpowerup(self):
        return self.__powerup

    def getscore(self):
        return self.__score

    def getlives(self):
        return self.__lives

    def release(self):
        self.__onhold.sethold(False)
        self.__onhold = 0

    def gethold(self):
        return self.__onhold

    def sethold(self, ball):
        self.__onhold = ball

    def declives(self):
        if self.__lives > 1:
            self.__lives -= 1
            self.__powerup = 0
        else:
            pass
            # os.system('clear')
            # quit()
