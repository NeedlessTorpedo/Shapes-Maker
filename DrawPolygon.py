import turtle
import time

#Draw Polygon Function
def drawPolygon(wn, turtleName, sideLength, sides):
    wn = turtle.Screen()                        #Creates a tkinter window
    wn.bgcolor("lightgreen")                    #Background Color
    turtleName = turtle.Turtle()                #Creates the turtle
    turtleName.speed(0)                         #Speed of the turtle
    angleTurn = 360/sides                       #Degree of angle

    for _ in range(sides):
        turtleName.left(angleTurn)
        turtleName.forward(sideLength)
    wn.exitonclick()

#Draw Circle Function
def drawCircle(turtleName, radius):
    circumference = 2 * 3.14 * radius           #Circumference of the circle
    sideLength = circumference / 360            #Length of each side of the circle
    drawPolygon('wn', turtleName, sideLength, 360)




typeOfShape = input("What type of shape do you want?? ((Polygon // Circle))")

#Output if polygon
if typeOfShape == 'Polygon':
    sideLength = int(input("Input length of sides here >>"))
    sides = int(input("Input the number of sides here >>"))
    drawPolygon('wn','john', sideLength, sides)

#Output if circle
elif typeOfShape == 'Circle':
    radius = int(input("Input the number of radius here >>"))
    drawCircle('john', radius)

else:
    print("No such shape exists!")

