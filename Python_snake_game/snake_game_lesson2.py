#We will add the food and food position

#Simple snake game in python 3 for begginners
import turtle
import time #We using time module to set moving time
import random
delay=0.1


#Set up the screen
wn=turtle.Screen()
wn.title("Snake game by Mr.AK")
wn.bgcolor("#5882FA")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off the screen updates

#Snake head use turtle object  
head=turtle.Turtle()
head.speed(0) #This is animation speed not turtle
head.shape("square")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction="stop"

#Snake food use turtle object  
food=turtle.Turtle()
food.speed(0) #This is animation speed not turtle
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)



#Functions to control directions
def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"

"""
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
"""
#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


#Function to move turtle
def move():
    if head.direction == "up":
        y =head.ycor() #Take current y coordinate
        head.sety( y+20)

    if head.direction == "down":
        y =head.ycor() #Take current y coordinate
        head.sety( y-20)

    if head.direction == "left":
        x =head.xcor() #Take current x coordinate
        head.setx( x-20)

    if head.direction == "right":
        x =head.xcor() #Take current x coordinate
        head.setx( x+20)


#Main game loop
while True:
    wn.update() #Everytime update the screen then we can see the snake

    if head.distance(food)<20: #We are using ready pythagorean function to measure distance between  food and snake. If distance is less than 20 that means tey are collided.
        #Move the food to a random position. Use random module. 'import random'
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)


    
    move()
    
    time.sleep(delay)

wn.mainloop() #this is for end keep screen on.