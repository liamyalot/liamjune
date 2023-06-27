import turtle
import time
from playsound import playsound
import random

def left():
    global moveShipBy
    moveShipBy = -3
    
def right():
    global moveShipBy
    moveShipBy = 3
    
def space():
    global bullet
    global spaceship
    
    if bullet.isvisible() == False:
        bullet.goto(spaceship.xcor(), spaceship.ycor()+45)
        bullet.showturtle()
        playsound("laser.wav", False)
        
#getEnemies create a list of enemy turtles and sets their positions
def getEnemies():
    e = None
    enemies = []
    for x in range(1,26):
        e = turtle.Turtle()
        e.hideturtle()
        e.shape("enemy.gif")
        e.penup()
        e.goto(random.randint(-350, 350), int(800*x))
        e.showturtle()
        enemies.append(e)
    
    return enemies

#define a function that calculates the number of pixels between two point on an axis
def pixelsBetween(value1, value2):
    if value1 > value2:
        return value1 - value2
    else:
        return value2 - value1
 
#define a function to create a list of counters to count how many times an explosion has been
#displayed
def getExplosionCounterList(enemyCount):
    counterList = []
    for i in range(enemyCount):
        counterList.append(0)
        
    return counterList

#enable and register keyboard events
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

win = turtle.Screen()
win.title("SPACE BLASTER")
win.setup(800, 600)
win.bgpic("space-bg.gif")
win.tracer(0)

#register graphic with turtle graphics
turtle.register_shape("ship.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("explosion.gif")

#create a turtle for my ship
spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

#create a turtle for my bullet laser blast
bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape("bullet.gif")
bullet.penup()

#get a list of enemies
enemies = getEnemies()

#get a list of counters to count how many times an explosion has been shown
explosionCounters = getExplosionCounterList(len(enemies))

moveShipBy = 0

#game loop that redraws our screen each time the loop executes
while True:
    
    spaceship.forward(moveShipBy)
    
    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(25)
        
    if bullet.ycor() > (win.window_height()/2):
        bullet.hideturtle()
    
    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0
    
    #animate our enemies from the top of the screen to the bottom
    enemyIndex = 0
    for enemy in enemies:
        if (enemy.ycor() > -350):
            enemy.setheading(270)
            enemy.forward(3)
            
        if (pixelsBetween(enemy.xcor(), bullet.xcor()) < 35 and
            pixelsBetween(enemy.ycor(), bullet.ycor()) < 35 and
            bullet.isvisible() and enemy.isvisible()):
            enemy.shape("explosion.gif")
            bullet.hideturtle()
            playsound("explosion.wav", False)            
            explosionCounters[enemyIndex] = 1
            
        if explosionCounters[enemyIndex] >= 1:
            explosionCounters[enemyIndex] = explosionCounters[enemyIndex] + 1
            
        if explosionCounters[enemyIndex] > 5:
            enemy.hideturtle()
        
        enemyIndex = enemyIndex + 1
        
            
    
    win.update()
    time.sleep(0.02)
