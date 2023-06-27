import turtle
import time
from playsound import playsound
import random

def left():
    global moveShipBy
    moveShipBy = -4
    
def right():
    global moveShipBy
    moveShipBy = 4
    
def space():
    global bullet
    global spaceship
    
    if bullet.isvisible() == False:
        playsound('laser.wav', False)
        bullet.setpos(spaceship.xcor(), spaceship.ycor()+45)
        bullet.showturtle()
        
def makeEnemies():
    e = None
    enemies = []
    for x in range(1, 26):
        e = turtle.Turtle()
        e.hideturtle()
        e.shape('enemy.gif')
        e.penup()
        e.setpos(random.randint(-350, 350), int(800*x))
        e.showturtle()
        enemies.append(e)
        
    return enemies

def pixelsBetween(value1, value2):
    if (value1 > value2):
        return value1-value2
    else:
        return value2-value1

turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

win = turtle.Screen()
win.title("SPACE BLASTER")
win.setup(800,600)
win.bgpic('space-bg.gif')
win.tracer(0)

turtle.register_shape('ship.gif')
turtle.register_shape('bullet.gif')
turtle.register_shape('enemy.gif')
turtle.register_shape('explosion.gif')

spaceship = turtle.Turtle()
spaceship.shape('ship.gif')
spaceship.penup()
spaceship.setpos(0, -200)
spaceship.speed(0)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape('bullet.gif')
bullet.penup()

enemies = makeEnemies()

moveShipBy = 0

while True:
    spaceship.setheading(0)
    spaceship.forward(moveShipBy)
    
    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(35)
        
    if bullet.ycor() > (win.window_height() / 2):
        bullet.hideturtle()
    
    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0
        
    for enemy in enemies:
        if (enemy.ycor() > -350):
            enemy.setheading(270)
            enemy.forward(3)
            
        if (pixelsBetween(enemy.xcor(), bullet.xcor()) < 35 and
           pixelsBetween(enemy.ycor(), bullet.ycor()) < 50 and
           bullet.isvisible()):
               enemy.shape('explosion.gif')
               playsound('explosion.wav', False)
               bullet.hideturtle()
               enemy.tiltangle(1)
               
        if (enemy.tiltangle() > 40):
            enemy.hideturtle()
        elif (enemy.tiltangle() > 0):
            enemy.tilt(enemy.tiltangle()+1)
           
    
    win.update()
    time.sleep(0.02)
    
    
    



