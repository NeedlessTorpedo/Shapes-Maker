import turtle
import time

def drawPolygon(wn, turtleName, sideLength, sides):
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    turtleName = turtle.Turtle()
    turtleName.speed(0)

    angleTurn = 360/sides

    for _ in range(sides):
        turtleName.left(angleTurn)
        turtleName.forward(sideLength)
    wn.exitonclick()

def drawCircle(turtleName, radius):
    circumference = 2 * 3.14 * radius
    sideLength = circumference / 360
    drawPolygon('wn', turtleName, sideLength, 360)




typeOfShape = input("What type of shape do you want?? ((Polygon // Circle))")

if typeOfShape == 'Polygon':
    sideLength = int(input("Input length of sides here >>"))
    sides = int(input("Input the number of sides here >>"))
    drawPolygon('wn','john', sideLength, sides)

elif typeOfShape == 'Circle':
    radius = int(input("Input the number of radius here >>"))
    drawCircle('john', radius)

else:
    print("No such shape exists!")

