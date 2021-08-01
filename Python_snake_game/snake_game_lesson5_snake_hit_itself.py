#Snake moving around eating apple and growing.
#We have completed 4th Lesson The snake head dying if The snake head the walls or border
#5th lesson we will check if the snake touch itself 

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

#We need an array to make the snake body.
#When the snake touch the apple (body)segment will grow
segments = []

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
#This Functions to control directions
#If the snake going down if i try to go up won't work
def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction="left":
        head.direction="right"

"""
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

    #Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        #Hide the segments when the snake hit the wall or border
        for segment in segments: #Goes through from o to all
            segment.goto(1000, 1000) 
        #When we hit the wall game stop but still segments there. 
        # We need to clear the segments
        segments.clear()    

    #Check for a collision with the food
    if head.distance(food)<20: #We are using ready pythagorean function to measure distance between  food and snake. If distance is less than 20 that means tey are collided.
        #Move the food to a random position. Use random module. 'import random'
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0) #This is animation speed not the snake move speed
        new_segment.shape("square")
        new_segment.color("brown") #body color
        new_segment.penup() #This segment will not draw anthing
        segments.append(new_segment)  #Adding segment to the arrays segments
    
    #Segments is a list or array can get bigger.
    #Segment is a turtle and The segment will make the snake body.
    # Move the end segments first in reverse order.    
    #If we have 5 segments in the body when add segment 6 segment 6 will  move segment 5
    for index in range(len(segments)-1, 0, -1): #This for loop start end to 0 and decrease by 1
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)





    
    move()

    #Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #Hide the segments when the snake hit the wall or border
            for segment in segments: #Goes through from o to all
                segment.goto(1000, 1000) 
            #When we hit the wall game stop but still segments there. 
            # We need to clear the segments
            segments.clear()    
    
    time.sleep(delay)

wn.mainloop() #this is for end keep screen on.