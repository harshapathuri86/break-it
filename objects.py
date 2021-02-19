import random
import os
from screen import *


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

    def display(self, shape):
        for i in range(self.__x, self.__x + len(shape)):
            for j in range(self.__y, self.__y + len(shape[0])):
                try:
                    display.grid[i][j] = shape[i - self.__x][j - self.__y]
                except:
                    print("ERR")
                    print(shape)
                    print(i, j, self.__x, self.__y)
                    quit()


class Brick(Object):

    def __init__(self, x, y, brick_type):
        self.__type = brick_type
        Object.__init__(self, x, y)

    def gettype(self):
        return self.__type

    def settype(self, brick_type):
        self.__type = brick_type

    def checkcollision(self):
        for ball in BALLS:
            type, x, y = ball.getbt()
            if type == 0:
                continue
            if self.__type != type:
                continue
            if type == 4 and not ball.getthru():
                continue
            bx = x - self.getx()
            by = y - self.gety()
            # if bx >= 0 and bx < brick_height and by >= 0 and by < brick_length:
            if 0 <= bx < brick_height and 0 <= by < brick_length:
                if ball.getthru():
                    self.settype(0)
                else:
                    self.settype(type - 1)
                if self.gettype() == 0:
                    newpower = Powerup(
                        self.getx(), self.gety(), random.randint(1, 6))
                    newpowerups.append(newpower)
                return
        self.display(BRICKS[self.gettype()])


class Ball(Object):
    def __init__(self, x, y, x_velocity, y_velocity):
        self.__x_v = x_velocity
        self.__y_v = y_velocity
        self.__collided_brick_type = 0
        self.__collided_brick_x = 0
        self.__collided_brick_y = 0
        self.__onhold = False
        self.__thru = False
        Object.__init__(self, x, y)

    def setxv(self, x_velocity):
        self.__x_v = x_velocity

    def getxv(self):
        return self.__x_v

    def setthru(self, thru):
        self.__thru = thru

    def getthru(self):
        return self.__thru

    def getbt(self):
        return self.__collided_brick_type, self.__collided_brick_x, self.__collided_brick_y

    def sethold(self, value):
        self.__onhold = value

    def gethold(self):
        return self.__onhold

    def setyv(self, y_velocity):
        self.__y_v = y_velocity

    def incspeed(self):
        y = self.getyv()
        x = self.getxv()
        if y > 0:
            self.setyv(y + 2)
        else:
            self.setyv(y - 2)
        if x > 0:
            self.setxv(x + 2)
        else:
            self.setxv(x - 2)

    def decspeed(self):
        y = self.getyv()
        x = self.getxv()
        if y > 0:
            self.setyv(y - 2)
        else:
            self.setyv(y + 2)
        if x > 0:
            self.setxv(x - 2)
        else:
            self.setxv(x + 2)

    def getyv(self):
        return self.__y_v

    def create_newball(self, paddle):
        yp = paddle.gety()
        yb = random.randint(yp, yp + paddle_sizes[paddle.gettype()])
        # ball = Ball(Screen_height-5, yb, -1, 1)
        ball = Ball(Screen_height - 5, yb, -1, 1)
        paddle.sethold(ball)
        BALLS.append(ball)
        # BALLS.remove(self)
        return

    def checkcollision(self, paddle):
        if self.__onhold:
            self.display(BALL)
            return
        diry = 0
        jv = self.getyv()
        iv = self.getxv()
        i = self.getx()
        j = self.gety()
        if jv < 0:
            diry = -1
        else:
            diry = 1
        dirx = 0
        if iv < 0:
            dirx = -1
        else:
            dirx = 1
        # print(j,jv,diry,i,iv,dirx)
        for y in range(j, j + jv + diry, diry):
            for x in range(i, i + iv + dirx, dirx):
                # check border
                # print("XY",x,y)
                check = False
                if x < 0:
                    self.setxv(-self.getxv())
                    self.setx(0)
                    check = True
                elif x >= Screen_height - 1:
                    self.setx(Screen_height - 2)
                    self.setxv(-self.getxv())
                    BALLS.remove(self)
                    if len(BALLS) == 0:
                        paddle.declives()
                        self.create_newball(paddle)
                    check = True
                if y < 0:
                    self.setyv(-self.getyv())
                    self.sety(0)
                    check = True
                elif y > Screen_width - 1:
                    self.setyv(-self.getyv())
                    self.sety(Screen_width - 1)
                    check = True
                if check:
                    self.display(BALL)
                    return
                # check brick
                val = 0
                try:
                    val = BRICKTYPES.index(display.grid[x][y])
                except:
                    val = 0
                if val > 0:
                    # found brick
                    # need to update collision strategy, should not check full rectangle !!!
                    # change to something using ratio
                    paddle.addscore(val)
                    self.__collided_brick_type = val
                    self.__collided_brick_x = x
                    self.__collided_brick_y = y
                    if self.__thru:
                        self.setx(self.getx() + self.getxv())
                        self.sety(self.gety() + self.getyv())
                        self.display(BALL)
                        return
                    posy = diry * (y - self.gety())
                    posx = dirx * (x - self.getx())
                    if posx == posy:
                        self.sety(y - diry)
                        self.setx(x - dirx)
                        self.setxv(-self.getxv())
                        self.setyv(-self.getyv())
                    elif posx > posy:
                        self.sety(y)
                        self.setx(x - dirx)
                        self.setxv(-self.getxv())
                    elif posx < posy:
                        self.setyv(-self.getyv())
                        self.sety(y - diry)
                        self.setx(x)
                    self.display(BALL)
                    return
                elif Screen_height > x > 0 and Screen_width > y > 0:
                    try:
                        if display.grid[x][y] == PADDLE:
                            # add variey of speed in y
                            mid = paddle.gety() + \
                                  int(paddle_sizes[paddle.gettype()] / 2)
                            self.sety(y)
                            self.setx(x - dirx)
                            self.setxv(-self.getxv())
                            self.setyv(self.getyv() + y - mid)
                            if paddle.getpaddlehold():
                                paddle.sethold(self)
                            self.display(BALL)
                            return
                    except:
                        pass
        self.setx(self.getx() + self.getxv())
        self.sety(self.gety() + self.getyv())
        self.display(BALL)


class Paddle(Object):
    def __init__(self, x, y, type):
        self.__type = type
        self.__lives = 3
        self.__score = 0
        self.__onhold = []
        self.__paddlehold = False
        Object.__init__(self, x, y)

    def settype(self, type):
        self.__type = type

    def gettype(self):
        return self.__type

    def setpaddlehold(self, paddlehold):
        self.__paddlehold = paddlehold

    def getpaddlehold(self):
        return self.__paddlehold

    def addscore(self, add):
        if add == 1:
            self.__score += 10
        elif add == 2:
            self.__score += 15
        elif add == 3:
            self.__score += 20
        # elif add == 4:

    def getscore(self):
        return self.__score

    def moveleft(self):
        if self.gety() - paddle_step >= 0:
            self.sety(self.gety() - paddle_step)
            try:
                for ball in self.__onhold:
                    ball.sety(ball.gety() - paddle_step)
            except:
                print(self.__onhold)
                quit()
        else:
            for ball in self.__onhold:
                if ball.gety() != 0:
                    ball.sety(ball.gety() - self.gety())
            self.sety(0)

    def moveright(self):
        if self.gety() + paddle_sizes[self.__type] + paddle_step <= Screen_width:
            self.sety(self.gety() + paddle_step)
            for ball in self.__onhold:
                ball.sety(ball.gety() + paddle_step)
        else:
            for ball in self.__onhold:
                if self.gety() != (Screen_width - paddle_sizes[self.__type]):
                    ball.sety(ball.gety() + Screen_width - paddle_sizes[self.__type] - self.gety())
            self.sety(Screen_width - paddle_sizes[self.__type])

    def getlives(self):
        return self.__lives

    def release(self):
        self.__onhold[0].sethold(False)
        self.__onhold.pop(0)

    def gethold(self):
        return self.__onhold

    def sethold(self, ball):
        self.__onhold.append(ball)
        ball.sethold(True)

    def declives(self):
        if self.__lives > 1:
            self.__lives -= 1
            while len(newpowerups):
                newpowerups.pop()
            for pow in powerups:
                if pow.getstatus() == 1:
                    pow.deactivate(self)
        else:
            # pass
            os.system('tput reset')
            print("GAME OVER")
            quit()


class Powerup(Object):
    def __init__(self, x, y, type):
        self.__timer = 0
        self.__status = 0
        self.__type = type
        Object.__init__(self, x, y)

    def getstatus(self):
        return self.__status

    def gettype(self):
        return self.__type

    def setstatus(self, status):
        self.__status = status

    def addtimer(self):
        self.__timer += 50

    def setzero(self):
        self.__timer = 0

    def dectimer(self):
        self.__timer -= 1
        if self.__timer == 0:
            return True
        return False

    def gettimer(self):
        return self.__timer

    # def kill(self):
    #     powerups.remove(self)
    def deactivate(self):
        self.setstatus(0)

    def activate(self, paddle):
        type = self.gettype()
        # print("TYPE",type,self.getx(),self.gety())
        # print(len(powerups),type)
        pow = powerups[type - 1]
        if pow.getstatus() == 0:
            pow.setstatus(1)
        pow.addtimer()

    def check(self, paddle):
        x = self.getx()
        y = self.gety()
        if display.grid[x + 1][y] == PADDLE:
            self.activate(paddle)
            return True
            # true to kill
        else:
            # print("X", self.getx())
            if self.getx() >= Screen_height - 2:
                return True
                # to kill
            self.setx(self.getx() + 1)
            self.display(POWERUPS[self.gettype() - 1])
            return False


class expandpaddle(Powerup):

    def __init__(self):
        Powerup.__init__(self, 0, 0, 0)

    def deactivate(self, paddle):
        self.setstatus(0)
        self.setzero()
        paddle.settype(1)

    def activate(self, paddle):
        # not working (paddle at right border)
        if self.getstatus() == 1:
            sz = paddle.gety() + len(PADDLES[2])
            if sz >= Screen_width:
                paddle.sety(paddle.gety() + sz - Screen_width)
            paddle.settype(2)
            if self.dectimer():
                self.deactivate(paddle)


class shrinkpaddle(Powerup):

    def __init__(self):
        Powerup.__init__(self, 0, 0, 1)

    def deactivate(self, paddle):
        self.setstatus(0)
        self.setzero()
        paddle.settype(1)

    def activate(self, paddle):
        if self.getstatus() == 1:
            paddle.settype(0)
            if self.dectimer():
                self.deactivate(paddle)


class doubletrouble(Powerup):

    def __init__(self):
        Powerup.__init__(self, 0, 0, 2)

    def deactivate(self, paddle):
        # print("LOLOL")
        self.setstatus(0)
        # print(len(BALLS),"BALLS")
        if len(BALLS) == 2:
            BALLS.pop(1)
        self.setzero()

    def activate(self, paddle):
        # print("status",self.getstatus())
        if self.getstatus() == 1:
            if len(BALLS) == 1:
                # pass
                # add ball
                b = BALLS[0]
                if b.getx() < Screen_height - 2:
                    BALLS.append(Ball(b.getx(), b.gety(), b.getxv(), -b.getyv()))
                else:
                    self.deactivate(paddle)
            if self.dectimer():
                self.deactivate(paddle)
            # print("TIMER",self.gettimer())
        else:
            self.deactivate(paddle)


class fastball(Powerup):

    def __init__(self):
        self.lol = 0
        Powerup.__init__(self, 0, 0, 3)

    def deactivate(self, paddle):
        # pass
        self.setstatus(0)
        self.lol = 0
        for ball in BALLS:
            ball.decspeed()
        self.setzero()

    def activate(self, paddle):
        if self.getstatus() == 1:
            if self.lol == 0:
                self.lol = 1
                for ball in BALLS:
                    ball.incspeed()
            if self.dectimer():
                self.deactivate(paddle)
            # print("TIMER", self.gettimer())
        # else:
        #     self.deactivate()


class thruball(Powerup):

    def __init__(self):
        Powerup.__init__(self, 0, 0, 4)

    def deactivate(self, paddle):
        self.setstatus(0)
        for ball in BALLS:
            ball.setthru(False)
        self.setzero()

    def activate(self, paddle):
        if self.getstatus() == 1:
            # code
            for ball in BALLS:
                ball.setthru(True)
            if self.dectimer():
                self.deactivate(paddle)
        else:
            self.deactivate(paddle)


class paddlegrab(Powerup):

    def __init__(self):
        Powerup.__init__(self, 0, 0, 5)

    def deactivate(self, paddle):
        self.setstatus(0)
        paddle.setpaddlehold(False)
        self.setzero()

    def activate(self, paddle):
        if self.getstatus() == 1:
            paddle.setpaddlehold(True)
            if self.dectimer():
                self.deactivate(paddle)
        else:
            self.deactivate(paddle)
