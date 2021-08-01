import turtle #First add turtle module.
ak = turtle.Turtle() #Decleare turtle object and give a name
ak.color('blue', 'red')
ak.shape('turtle') #Changed shape as a turtle.
#We can change the background we can add a GIF format picture.
#The GIF picture must be in same folder with the our python file.
wn = turtle.Screen()  #We set a screen module
wn.bgpic('bg.gif')



wn.bgcolor('orange') #We set the window color.
turtle.colormode(255)
wn.bgcolor(58, 135, 76)
wn.title('Mr.Ak Python Class ')
ak.speed(0) #Speed fast
#How to use a gif picture instead of a turtle or a triangle.
image = "snakehead.gif"
wn.addshape(image)
ak.shape(image)

ak.forward(50)
ak.setheading(90)#Set the head direction.
#help(turtle.forward)
ak.forward(50)
ak.forward(-100)
ak.left(90)
ak.backward(100)
ak.right(90)
ak.backward(100)
ak.penup()
ak.left(90)
ak.forward(200)
ak.left(180)
ak.speed(0) #fast
ak.pendown()
ak.begin_fill()
ak.fillcolor('orange')
for i in range(4):
    ak.forward(50)
    ak.left(90)
ak.end_fill()    
ak.hideturtle() #We can hide the turtle.
ak.penup()
ak.forward(200)
ak.showturtle() #We can show the turtle.
ak.pendown()
ak.color('green', 'red')
#We can draw a circle circle(radius, extent=None, steps=None)
#circle(120, 180)   semicircle
ak.circle(50)
ak.circle(-50)
#We can reset everything. Thats mean run code code step by step when reset line active then everything will be clear.
ak.reset()

ak.begin_fill()
ak.fillcolor('red')
ak.circle(30, steps=5)
ak.end_fill()

ak.begin_fill()
ak.fillcolor('blue')
ak.circle(20, steps=3)
ak.end_fill()
ak.hideturtle()
ak.circle(50, extent=180, steps=3)

#We gonna learn how to use goto
ak.reset() #Clear everything on the canvas
ak.shape('turtle') #Change the turtle shape
ak.speed(0) #fast
ak.circle(50)
ak.undo()
help(turtle.undo) #you can get the command details.
ak.forward(100)
ak.goto(80, 100)
ak.circle(50)
ak.reset()
help(turtle.up)
#Pull the pen up -- no drawing when moving.
ak.up() 
ak.goto(100, 100)
#Pull the pen down --  Drawing when moving.
ak.down()
ak.circle(50)


#Make a function to draw circle with parameters coordinates, color, and radius
def draw_circle(x, y, color, radius):
    ak.goto(x,y)
    ak.down()
    ak.begin_fill()
    ak.fillcolor(color)
    ak.circle(radius)
    ak.end_fill()
    ak.up()
    ak.home()

ak.speed(0)
ak.pensize(5)
draw_circle(100, 100, "blue", 50)
draw_circle(-100, 100, "green", 50)
draw_circle(100, -100, "red", 50)
#Reset
ak.reset()
#Using array in a for loop to draw different color circle
color_list=["red", "blue", "yellow", "orange"]
ak.speed(0)
for i in range(4):
    ak.down()
    ak.begin_fill()
    ak.fillcolor(color_list[i])
    ak.circle(50)
    ak.end_fill()
    ak.up()
    ak.forward(100)

ak.reset()
#Using array in a for loop to draw different color circle
ak.up()
ak.speed(0)
ak.goto(-200,0)
color_list=["red", "blue", "yellow", "orange", "purple"]

for i in range(4):
    ak.down()
    ak.color(color_list[i])
    ak.pensize(30)
    ak.circle(50)
    ak.up()
    ak.bk(50)

ak.speed(0)
ak.up()
ak.goto(100,120)
ak.down()

for i in range(100):
    ak.color(color_list[i%3])
    ak.pensize((i/10)+1)
    ak.forward(i)
    ak.left(60)
ak.reset()
ak.speed(0)
for i in range(100):
    ak.color(color_list[i%5])
    ak.pensize( i/10+1)
    ak.forward(i)
    ak.left(59)



ak.speed(0)
ak.up()
ak.goto(-100,120)
ak.down()
color_list=["#5882FA", "#33FFFC", "#FF5833", "#9C33FF", "#E168C4"]
for i in range(100):
    ak.color(color_list[i%5])
    ak.pensize( i/10+1)
    ak.forward(i)
    ak.left(61)




    


