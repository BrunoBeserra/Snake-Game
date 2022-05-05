##### SNAKE GAME #####
## Bruno Beserra ##

# Import modules
import turtle
import time
import random

# Set Up the Game Screen
gameWindow = turtle.Screen()
gameWindow.title("Snake Game")
gameWindow.bgcolor("light green")
gameWindow.setup(width=600, height=600)
gameWindow.tracer(0)

# Set default values
delay = 0.05
bodyParts = []
score = 0
highScore = 0

# Create Snake Head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("navy blue")
snakeHead.penup()
snakeHead.goto(0, 50)
snakeHead.direction = "stop"

# Function Movements, to move the snake

def movements():
    if snakeHead.direction == "up":
        y = snakeHead.ycor() # Y coordinate of the snake
        snakeHead.sety(y + 20)

    if snakeHead.direction == "down":
        y = snakeHead.ycor() # Y coordinate of the snake
        snakeHead.sety(y - 20)

    if snakeHead.direction == "left":
        x = snakeHead.xcor() # Y coordinate of the snake
        snakeHead.setx(x - 20)

    if snakeHead.direction == "right":
        x = snakeHead.xcor() # Y coordinate of the snake
        snakeHead.setx(x + 20)


# Note: If the snake is moving in one direction, 
#       It cannot change it to the opposite direction.

def moveUp(): # It'll move up if doesn't moving down
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
 
def moveDown(): # It'll move down if doesn't moving up
    if snakeHead.direction != "up":
        snakeHead.direction = "down"

def moveLeft(): # It'll move left if doesn't moving right
    if snakeHead.direction != "right":
        snakeHead.direction = "left"

def moveRight(): # It'll move right if doesn't moving left
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

# Keyboard Controllers
gameWindow.listen()
gameWindow.onkey(moveUp, "w")
gameWindow.onkey(moveDown, "s")
gameWindow.onkey(moveRight, "d")
gameWindow.onkey(moveLeft, "a")

# Create Food
snakeFood = turtle.Turtle()
snakeFood.speed(0)
snakeFood.shape("circle")
snakeFood.color("crimson")
snakeFood.penup()
snakeFood.shapesize(0.5, 0.5)
snakeFood.goto(0, 0)

# Add Score
text = turtle.Turtle()
text.speed(0)
text.shape("square")
text.penup()
text.color("green")
text.hideturtle()
text.clear()
text.goto(0, 260)
text.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Create Snake Body
def newPart():
    newBodyPart = turtle.Turtle()
    newBodyPart.speed(0)
    newBodyPart.shape("square")
    newBodyPart.color("blue")
    newBodyPart.penup()
    bodyParts.append(newBodyPart)

# Get last body parts to move for previous spaces from firts parts
def bodyMovement():
    for index in range(len(bodyParts)-1, 0, -1):
        i = bodyParts[index-1].xcor()
        j = bodyParts[index-1].ycor()
        bodyParts[index].goto(i, j)
    if len(bodyParts) != 0:
        i = snakeHead.xcor()
        j = snakeHead.ycor()
        bodyParts[0].goto(i, j)    

# Main game loop
while True:
    gameWindow.update()
    # Check if Snake Collided with Stage Limits 
    if snakeHead.xcor() > 290 or snakeHead.xcor() < -290 or snakeHead.ycor() > 290 or snakeHead.ycor() < -290:
        time.sleep(1)
        snakeHead.goto(0, 50)
        snakeHead.direction = "stop"

        # Hide body parts
        for bodyPart in bodyParts:
                bodyPart.goto(1000, 1000)
        bodyParts.clear()
        score = 0
        text.clear()
        text.write("Score: {} High Score: {}".format(score, highScore),align="center", font=("Courier", 24, "normal"))

    # Check if snake eat the food
    if snakeHead.distance(snakeFood) < 15:        # Snake eat the food
        # Choose a random place for new food
        X = random.randint(-290, 290)
        Y = random.randint(-290, 290)
        snakeFood.goto(X, Y)
        # Add body to snake
        newPart()
        score += 10
        if score > highScore:
            highScore = score
        # Update text with Score
        text.clear()
        text.write("Score: {} High Score: {}".format(score,highScore), align="center", font=("Courier", 24, "normal"))
    # Body movement Function    
    bodyMovement()
    # Head movement Function
    movements()
    # Check body collision as well
    for bodyPart in bodyParts:
        if bodyPart.distance(snakeHead) < 20:
            time.sleep(1)
            snakeHead.goto(0, 50)
            snakeHead.direction = "stop"
        
        # Hide body parts
            for bodyPart in bodyParts:
                bodyPart.goto(1000, 1000)
            bodyParts.clear()
            score = 0
            text.clear()
            text.write("Score: {} High Score: {}".format(score, highScore),align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)

   