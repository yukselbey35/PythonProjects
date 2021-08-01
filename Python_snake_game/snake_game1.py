#Simple snake game in python 3 for begginners
import turtle
import time #We using time module to set moving time
delay=0.1


#Set up the screen
wn=turtle.Screen()
wn.title("Snake game by Mr.AK")
wn.bgcolor("#5882FA")
wn.bgpic("bgs.gif")
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
    
    move()
    
    time.sleep(delay)

wn.mainloop() #this is for end keep screen on.
