Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> First add turtle module
SyntaxError: invalid syntax
>>> #First add turtle module.
>>> ak = turtle.Turtle() #Decleare turtle object and give a name
>>> ak.shape('turtle')
>>> #Changed shape as a turtle.
>>> ak.color('red', 'blue')
>>> ak.forward(9)
>>> ak.forward(50)
>>> ak.color('blue', 'red')#Pen color is blue but turtle color is red
>>> ak.forward(30)
>>> wn = turtle.Screen() #We set a screen module
>>> wn.bgcolor('orange') #We set the window color.
>>> #We can set RGB color.
>>> turtle.colormode() #Check the color mode
1.0
>>> turtle.colormode(255)
>>> #Now we can use RGB color
>>> wn.bgcolor(58, 135, 76)
>>> #We can change the screen title
>>> wn.title('Mr. Ak Python Class)

>>> wn.title('Mr. Ak Python Class')
>>> #We can change the background we can add a GIF format picture.
>>> #The GIF picture must be in same folder with the our python file.
>>> wn = turtle.Screen()
>>> wn.bgpic('bg1.gif')

