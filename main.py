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
        playsound("kiblast.mp3", False)
        
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

def pixelsBetween(value1, value2):
    if value1 > value2:
        return value1 - value2
    else:
        return value2 - value1
    
def getExplosionCounterList(enemyCount):
    counterList = []
    for i in range(enemyCount):
        counterList.append(0)        
    return counterList
        
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

scr = turtle.Screen()
scr.title("SPACE ATTACK")
scr.setup(800,600)
scr.bgpic("gokuBG.PNG")
scr.tracer(0)

turtle.register_shape("ship.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("explosion.gif")

spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape("bullet.gif")
bullet.penup()

enemies = getEnemies()

explosionCounters = getExplosionCounterList(len(enemies))

moveShipBy = 0
points = 0
enemiesRemaining = len(enemies)

scoreTurtle = turtle.Turtle()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.pencolor("black")

scoreTurtle.goto(375, 250)
scoreTurtle.write(f"Score: {points}", align="right", font=("Arial", 25, "bold"))

while enemiesRemaining > 0:
    
    spaceship.forward(moveShipBy)
    
    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(25)
        
    if bullet.ycor() > (scr.window_height()/2):
        bullet.hideturtle()
    

    
    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0
    enemyIndex = 0
    enemiesRemaining = 0
    for enemy in enemies:
        if (enemy.ycor() > -350):
            enemy.setheading(270)
            enemy.forward(3)
            enemiesRemaining = enemiesRemaining + 1
            
            
                
        if (pixelsBetween(enemy.xcor(), bullet.xcor()) < 35 and
                pixelsBetween(enemy.ycor(), bullet.ycor()) < 35 and
                bullet.isvisible() and enemy.isvisible()):
            enemy.shape("explosion.gif")
            bullet.hideturtle()
            playsound("explosion-meme_dTCfAHs.mp3", False)
            explosionCounters[enemyIndex] = 1
            points = points + 1000
            scoreTurtle.clear()
            scoreTurtle.write(f"Score: {points}", align="right", font=("Arial", 25, "bold"))
                
        if explosionCounters[enemyIndex] >= 1:
            explosionCounters[enemyIndex] = explosionCounters[enemyIndex] + 1
                                 
        if explosionCounters[enemyIndex] > 5:
            enemy.hideturtle()

                
        enemyIndex = enemyIndex + 1
                
    
    scr.update()
    time.sleep(0.009)
    
scoreTurtle.goto(0,0)
scoreTurtle.write("GAME OVER", align= "center", font=("Arial", 50, "bold"))