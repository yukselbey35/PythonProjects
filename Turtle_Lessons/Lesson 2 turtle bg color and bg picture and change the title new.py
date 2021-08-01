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


    


