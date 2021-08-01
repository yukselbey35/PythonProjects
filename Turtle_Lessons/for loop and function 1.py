# Python program to draw  
# Spiral Square Outside In and Inside Out  
# using Turtle Programming 
import turtle   #Outside_In 
wn = turtle.Screen() 
wn.bgcolor("light green") 
wn.title("Turtle") 
skk = turtle.Turtle() 
skk.color("blue") 
skk.speed(0)
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size-5
  
sqrfunc(146) 
sqrfunc(126) 
sqrfunc(106) 
sqrfunc(86) 
sqrfunc(66) 
sqrfunc(46) 
sqrfunc(26) 



skk.clear()
  
def sqrfunc(size): 
    for i in range(4): 
        skk.fd(size) 
        skk.left(90) 
        size = size + 5
  
sqrfunc(6) 
sqrfunc(26) 
sqrfunc(46) 
sqrfunc(66) 
sqrfunc(86) 
sqrfunc(106) 
sqrfunc(126) 
sqrfunc(146) 
