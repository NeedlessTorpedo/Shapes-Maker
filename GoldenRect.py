#import  turtle module
import turtle
#import math module
import math

#creates the window and the turtle 
wn = turtle.Screen()                               
wn.bgcolor("Lavender")
trtl = turtle.Turtle()

#Length of sides
lngth = 100

#Draws a Square
for i in range(4):                                        
    trtl.left(360/4)
    trtl.forward(lngth)                                     
trtl.backward(lngth/2)

# Angle of the golden triangle  **Law of Sine** ((sin90)/(math.sqrt(5)/2) = (sinA)/1)
trtl.left(63.43)

#Square root of 5 divided by 2 is multiplied by length of side
trtl.forward((math.sqrt(5)/2)*lngth)                        

trtl.backward((math.sqrt(5)/2)*lngth)
trtl.right(63.43)

trtl.forward((math.sqrt(5)/2)*lngth)
trtl.left(90)
trtl.forward(lngth)
trtl.left(90)
trtl.forward(((math.sqrt(5)/2)*lngth))

wn.exitonclick()

