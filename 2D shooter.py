from turtle import *
from random import randint
from time import sleep

a=50
cd=0
ecd=0
b=0
class Bullet(Turtle):
    def __init__(self,color):
        super().__init__()
        self.ht()
        self.color(color)
        self.shape('circle')
        self.step=10
        self.up()
        self.speed(15)
class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('turtle')
        self.step=1
        self.up()
        self.speed(5)
        self.goto(-100,100)
    def idk(self,player):
        self.setheading(self.towards(player))
        self.fd(self.step)
    def eshoot(self):
        global ecd
        if ecd<=0:
            bullet=Bullet('red')
            bullet.goto(self.xcor(),self.ycor())
            bullet.st()
            bullet.setheading(self.heading())
            def move():
                global b
                bullet.fd(3)
                if abs(bullet.xcor() - player.xcor()) < 20 and abs(bullet.ycor() - player.ycor()) < 20:
                    b -= 1
                    enemy.clear()
                    enemy.write(a, align='center', font=('Arial', 12, 'bold'))
                    bullet.ht()
                if abs(bullet.xcor()) < 300 and abs(bullet.ycor()) < 300:
                    scr.ontimer(move, 20)
                else:
                    bullet.ht()
                    if bullet in scr._turtles:
                        scr._turtles.remove(bullet)
                    return
            move()
            ecd=60
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.shape('turtle')
        self.up()
        self.speed(13)
        self.step=10
    def Up(self):
        self.setheading(90)
        self.goto(self.xcor(),self.ycor()+self.step)
    def Down(self):
        self.setheading(270)
        self.goto(self.xcor(),self.ycor()-self.step)
    def Right(self):
        self.setheading(0)
        self.goto(self.xcor()+self.step,self.ycor())
    def Left(self):
        self.setheading(180)
        self.goto(self.xcor()-self.step,self.ycor())
    def shoot(self):
        global cd
        if cd<=0:
            bullet=Bullet('yellow')
            bullet.goto(self.xcor(),self.ycor())
            bullet.st()
            bullet.setheading(self.heading())
            def move():
                global a
                bullet.fd(5)
                if abs(bullet.xcor() - enemy.xcor()) < 20 and abs(bullet.ycor() - enemy.ycor()) < 20:
                    a -= 1
                    enemy.clear()
                    enemy.write(a, align='center', font=('Arial', 12, 'bold'))
                    bullet.ht()
                    if bullet in scr._turtles:
                        scr._turtles.remove(bullet)
                if abs(bullet.xcor()) < 300 and abs(bullet.ycor()) < 300:
                    scr.ontimer(move, 20)
                else:
                    bullet.ht()
                    if bullet in scr._turtles:
                        scr._turtles.remove(bullet)
                    return
            move()
            cd=20
player=Player()
enemy=Enemy()
scr=player.getscreen()
scr.tracer(0)
scr.onkey(player.Up,'w')
scr.onkey(player.Down,'s')
scr.onkey(player.Right,'d')
scr.onkey(player.Left,'a')
scr.onkey(player.shoot,'e')
scr.listen()
game_over = False
def game_loop():
    global cd
    global ecd
    global game_over
    if game_over:
        return
    enemy.idk(player)
    if (abs(enemy.xcor() - player.xcor()) < 20 and abs(enemy.ycor() - player.ycor()) < 20) or b!=0:
        player.write('Проигрыш', align='center', font=('Arial', 24, 'bold'))
        game_over = True
        return
    if a <= 0:
        player.write('Победа!', align='center', font=('Arial', 24, 'bold'))
        enemy.ht()
        game_over = True
        return
    scr.update()
    scr.ontimer(game_loop, 30)
    if cd>0:
        cd-=1
    if ecd>0:
        ecd-=1
    enemy.eshoot()
game_loop()
done()