import turtle
ak = turtle.Turtle()
#We can change the background we can add a GIF format picture.
#The GIF picture must be in same folder with the our python file.
wn = turtle.Screen()
wn.bgpic('bg.gif')
ak = turtle.Turtle() #Decleare turtle object and give a name
ak.shape('turtle')
#Changed shape as a turtle.
ak.color('red', 'blue')
ak.forward(9)
ak.forward(50)
ak.color('blue', 'red')#Pen color is blue but turtle color is red
ak.forward(30)
wn = turtle.Screen() #We set a screen module
wn.bgcolor('orange') #We set the window color.
#We can set RGB color.
turtle.colormode() #Check the color mode
turtle.colormode(255)
#Now we can use RGB color
wn.bgcolor(58, 135, 76)
#We can change the screen title
wn.title('Mr. Ak Python Class')
