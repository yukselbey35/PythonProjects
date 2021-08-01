import turtle 
loadWindow = turtle.Screen() 
turtle.speed(0)

#A square spiral program:
for i in range(200): # this "for" loop will repeat these functions 500 times
    turtle.forward(i)
    turtle.left(91)
turtle.reset()
turtle.speed(0)

# Python program to draw  
# Spiral  Helix Pattern 
# using Turtle Programming 
for i in range(100): 
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 


