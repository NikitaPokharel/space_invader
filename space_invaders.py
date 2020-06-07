# Space Invaders 
# Set up the screen
import turtle
import os
import math
import sys
import random
import winsound

# Set up the screen
main_screen = turtle.Screen()
main_screen.bgcolor('black')
main_screen.title('Space Invaders')
main_screen.bgpic('space_invaders_background.gif')
main_screen.tracer(0)

# Register the shapes
main_screen.register_shape('invader.gif')
main_screen.register_shape('player.gif')

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color ('White')
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = 'Score: {}'.format(score)
score_pen.write(scorestring, False, align ='left', font = ('Courier', 14, 'normal'))
score_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
# player.color ('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
 
player.speed = 0
enemyspeed = 0.1

# Chooose a number of enemies
number_of_enemies = 44
# Create an empty list of enemies
enemies = []

# Add enemies to  the list
for i in  range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -235
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
# Create the enemy
    # enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x +( 50* enemy_number)
    y = enemy_start_y 
    enemy.setposition(x, y)
    #Update the enemy number
    enemy_number += 1
    if enemy_number == 11:
        enemy_start_y -= 50
        enemy_number = 0

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 10

# Define bullet state
# ready - ready to fire
# fire - bullet  is firing
bulletstate = 'ready'

# Move the player left nd right
def move_left():
    player.speed = -2
    
def move_right():
    player.speed = 2

def move_player():
    x = player.xcor()
    x+= player.speed
    if x< -280:
        x = -280
    if x> 280:
        x = 280    
    player.setx(x)

def fire_bullet():
    # Declare  bulletstate as a global if its needs changed
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound('laser.wav', winsound.SND_ASYNC )
        bulletstate = 'fire'
        
        # Move the bullet to the just above the player
        x = player.xcor()  
        y = player.ycor() 
        bullet.setposition(x, y+10)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))        
    if distance < 15:
        return True
    else:
        return False   
    
# Create keyboard bindings
main_screen.listen()
main_screen.onkeypress(move_left, 'Left')
main_screen.onkeypress(move_right, 'Right')
main_screen.onkeypress(fire_bullet, 'space')
   
# Main game loop
while True: 
    main_screen.update()
    move_player()

    for enemy in enemies:
    # Move the enemy
        x =enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:  
            # Moves all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1            

        if enemy.xcor() <-280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y) 
            enemyspeed*= -1

        # Check for a  Collision between the  bullet and enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
            # Reset the bullet
            bullet.hideturtle()    
            bulletstate = 'ready'
            bullet.setposition(0, -250)

            # Reset the enemy
            enemy.setposition(0,10000)

            # Update the score
            score += 10
            score_pen.clear()
            score_pen.write('score: {}'.format (score), False, align ='left', font = ('Courier', 14, 'normal'))    

        if isCollision(player, enemy):
            winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle() 
            #For Gameover   
            Game_Over_pen = turtle.Turtle()
            Game_Over_pen.speed(0)
            Game_Over_pen.color('white')
            Game_Over_pen.penup()
            Game_Over_pen.setposition(0, 0)
            Game_Overstring = 'Game Over'
            Game_Over_pen.write(Game_Overstring, False, align ='center', font = ('Courier', 20, 'normal'))
            Game_Over_pen.hideturtle()
            exit()
            
    # Move the bullet
    if bulletstate =='fire':
        y = bullet.ycor()   
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate ='ready'


